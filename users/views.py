from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

from .models import Account

# Create your views here.
def signup(request):
    """Register a new user."""
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # if user is not None:
            login(request, new_user)
            return redirect('studypals:dashboard')  # Redirect to a success page

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

def login_view(request):
    """Log users in."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('studypals:chat')  # Redirect to a success page
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)