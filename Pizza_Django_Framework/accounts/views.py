from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from Pizza_Django_Framework.accounts.forms import LoginForm, RegisterForm, ProfileForm
from Pizza_Django_Framework.accounts.models import Profile
from Pizza_Django_Framework.pizza.models import Pizza


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def logout_user(request):
    logout(request)
    return redirect('dashboard')

@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    else:
        form = ProfileForm(instance=profile)

    user_pizzas = Pizza.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'user_pizzas': user_pizzas,
        'profile': profile,
    }
    return render(request, 'accounts/user_profile.html', context)