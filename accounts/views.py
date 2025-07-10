from django.contrib.auth import login,authenticate
from django.shortcuts import render
from django.urls import reverse
from .models import Profile
from .form import SignUpForm, UserForm, ProfileForm 
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializer import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User

# Create your views here.   
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             usr = authenticate (username=username, password=password)
#             login(request, usr)
#             return redirect('Profile')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html',{'form': form}) 

# def logout_view(request):
#     from django.contrib.auth import logout
#     logout(request)
#     return redirect('store:home')  # Redirect to home page after logout

# def profile(request):
#     profile = Profile.objects.get(user=request.user)
#     return render(request, 'accounts/profile.html', {'profile': profile})

# def profile_edit(request):
#     profile_edit = Profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         profileform = ProfileForm(request.POST, request.FILES, instance=profile_edit)
#         userform = UserForm(request.POST, instance=request.user)
#         if profileform.is_valid() and userform.is_valid():
#             profileform.save()
#             userform.save()     
#             return redirect(reverse('accounts:profile'))
#     else:
#         profileform = ProfileForm(instance=profile_edit)
#         userform = UserForm(instance=request.user)

#     return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform, 'profile_edit' : profile_edit})




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'  
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username' 