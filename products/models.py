from django.db import models
from django.utils.text import slugify
import uuid
from datetime import datetime

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"products/{datetime.now().strftime('%Y/%m/%d')}/{filename}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='products_created')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True, help_text="Unique URL slug for the product")
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def created_by_username(self):
        return self.created_by.username if self.created_by else "Unknown"
    
    class Meta:
        ordering = ["-created_at"]
        
        
        
        
