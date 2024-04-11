from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, CustomForm
from .models import UserProfile, ProfileStatus
from django.http import HttpResponse



def landing_view(request):
    
    context = {
        'title': 'home'
    }
    return render(request, 'base/landing_page.html', context)

# /////////
# CREATING, UPDATING AND DELETING LOAN REQUESTS
@login_required
def view_loan(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    stateTrue = ProfileStatus.objects.filter(status=True)
    stateFalse = ProfileStatus.objects.filter(status=False)
    stateNone = ProfileStatus.objects.filter(status=None)
    context = {
        'title': 'loan requests',
        'profile': profile,
        'stateTrue' : stateTrue,
        'stateFalse' : stateFalse,
        'stateNone' : stateNone
    }
    return render(request, 'base/loan_view.html', context)
    

@login_required
def create_loan(request):
    form = UserProfileForm()
    if request.method == 'POST':
      form = UserProfileForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('view_profile')
    #   else:
    #       form = UserProfileForm()
    context = {
        'title': 'create loan',
        'form': form
    }
    return render(request, 'base/loan_create.html', context)
        



@login_required
def update_loan(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)
    context = {
        'title': 'loan update',
        'form': form
    }
    return render(request, 'base/loan_update.html',context)

@login_required
def delete_loan(request, id):
    form = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        form.delete()
        return redirect('view_profile')
    context = {
        'title': 'loan delete',
    }
    return render(request, 'base/loan_delete.html', context)

# /////////
# UPDATING LOAN STATUS.


# /////////

def register_view(request):
  form = CustomForm()
  if request.method == 'POST':
    form = CustomForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.save()
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'register error')

  context={
      'form':form,
      'messages': messages,
      'title':'register'
    }
  return render(request, 'base/register.html',context)

   
def login_view(request):
    if request.user.is_authenticated:
            return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
             messages.error(request, 'username error!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'login credentials  missmatch!')
        
    context ={
    #   'form': form,
        'title':'login'
    }
    return render(request, 'base/login.html', context)

@login_required(login_url='login')
def delete_user_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'base/user_delete.html')

@login_required(login_url='login')
def profile_view(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        context ={
          'user_profile': user_profile,
          'title':request.user.username
        }
        return render(request, 'base/landing_page.html', context)
    else:
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('home')

# admin, zxcvbnm,./