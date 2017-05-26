from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def login (request):
    args = {}
    #args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "User %s is not found!" % username)
            #args['login_error'] = "User is not find!"
            return render(request, "login.html", args)
    else:
        return render(request, "login.html", args)

def logout (request):
    auth.logout(request)
    return  redirect('/')

def register (request):
    args={}
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect("room:add_character")
        else:
            args['form'] = new_user_form
    return  render(request, "register.html", args)
