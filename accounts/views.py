from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def logout(request):
    """Logout the User"""
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect(reverse('index'))
    
