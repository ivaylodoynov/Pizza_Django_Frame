from django.shortcuts import render, redirect

# Create your views here.
from Pizza_Django_Framework.pizza.models import Pizza
from Pizza_Django_Framework.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from Pizza_Django_Framework.profiles.models import Profile


def show_profile(request):
    profile = Profile.objects.first()
    pizzas_count = len(Pizza.objects.all())
    pizza = Pizza.objects.all()

    context = {
        'profile': profile,
        'pizzas_count': pizzas_count,
        'pizza': pizza,

    }
    return render(request, 'details-profile.html', context)

def create_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'create-profile.html', context)

def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)

def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        profile.delete()
        Pizza.objects.all().delete()
        return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)