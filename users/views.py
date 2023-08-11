from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
            form.save()
            username = form.cleaned_data['username']
            matric_no = form.cleaned_data['matric_no']
            dept = form.cleaned_data['dept']
            # password = form.cleaned_data['password1']
            user = User.objects.get(username=username)
            user_data = Account.objects.create(user=user, matric_no=matric_no, dept=dept)
            user_data.save()
            # login(request, authenticate(matric_no, password)
            return redirect('')


    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)