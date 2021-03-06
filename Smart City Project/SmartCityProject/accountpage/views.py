from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from accountpage.forms import editform
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.



def accountpage(request):
    if not request.user.is_authenticated:
        return redirect('/welcome/')
    usergroup = ""
    if request.user.groups.filter(name = 'Business').exists():
        usergroup = "Business"
    if request.user.groups.filter(name = 'Student').exists():
        usergroup = "Student"
    if request.user.groups.filter(name = 'Tourist').exists():
        usergroup = "Tourist"
    return render (request, 'accountpage.html', {'usergroup':usergroup})

def accounteditpage(request):
    if not request.user.is_authenticated():
        return redirect('/welcome/')
    if request.method == 'POST':
        form = editform(request.POST, instance = request.user)
        if form.is_valid():
            emailfield = form.cleaned_data['email']
            if (User.objects.filter(email=emailfield).exists() & (request.user.email != emailfield)):
                messages.error(request,'Email Already in use')
            else:
                user = form.save(commit = False)
                user.save()
                user.webuser.address = form.cleaned_data['address']
                user.webuser.phonenumber = form.cleaned_data['phonenumber']
                user.webuser.save()
                return redirect('/account/')
    else:
        # Insert default values into form
        form = editform({'email' : request.user.email, 'first_name' : request.user.first_name, 'last_name' : request.user.last_name, 'address' : request.user.webuser.address, 'phonenumber' : request.user.webuser.phonenumber}, instance = request.user)
    return render (request, 'accounteditpage.html', {'form' : form})

def accountchangepasswordpage(request):
    if not request.user.is_authenticated():
        return redirect('/welcome/')
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save();
            return redirect('/login/')
    else:
        form = PasswordChangeForm(user = request.user)
    return render (request, 'changepasswordpage.html', {'form' : form})
