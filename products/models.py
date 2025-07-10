from django.db import models
from django.utils.text import slugify
import uuid
from datetime import datetime
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db.models import F, Sum


def upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"products/{datetime.now().strftime('%Y/%m/%d')}/{filename}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    category = models.ForeignKey(
        "ProductCategory", on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="products_created"
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        help_text="Unique URL slug for the product",
    )
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def created_by_username(self):
        return self.created_by.username if self.created_by else "Unknown"

    def __str__(self):
        return self.name if self.name else "Unnamed Product"

    class Meta:
        ordering = ["-created_at"]


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,
                                 related_name="order")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_total_price(self):
        total_sum_result = self.items.aggregate(
            calculated_total=Sum(F('price') * F('quantity')))
        total_sum = total_sum_result.get('calculated_total', 0.00)
        self.total_amount = total_sum if total_sum is not None else 0.00
        self.save(update_fields=['total_amount'])

    def __str__(self):
        return f"""Order
    {self.id} - {self.customer.name if self.customer else 'No Customer'}"""


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    order = models.ForeignKey("Order", on_delete=models.CASCADE,
                              related_name="items")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if self.pk is None or self.price is None:
            self.price = self.product.price
        self.total = self.quantity * self.price
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.product.name


@receiver(post_save, sender=OrderItem)
def update_order_total(sender, instance, **kwargs):
    if instance.order:
        instance.order.update_total_price()


@receiver(pre_delete, sender=OrderItem)
def delete_order_item(sender, instance, **kwargs):
    if instance.order:
        instance.order.update_total_price()
