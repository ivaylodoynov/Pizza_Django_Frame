from django.shortcuts import render, redirect

from Pizza_Django_Framework.pizza.forms import CreatePizzaForm, DeletePizzaForm, EditPizzaForm
from Pizza_Django_Framework.pizza.models import Pizza
from Pizza_Django_Framework.profiles.models import Profile


def home_page(request):
    profile = Profile.objects.first()

    pizzas = Pizza.objects.all()

    context = {
        'pizzas': pizzas,
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def home_details(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('create profile') # tova e po name

    pizzas = Pizza.objects.all()

    context = {
        'pizzas': pizzas,
        'profile': profile,
    }

    return render(request, 'dashboard.html', context)

def create_pizza(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = CreatePizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard') #tova e po ime
        context = {'form': form, 'profile': profile}
        return render(request, 'create-pizza.html', context)

    form = CreatePizzaForm()
    context = {'form': form, 'profile': profile}
    return render(request, 'create-pizza.html', context)


def show_pizza_details(request, pizza_id):
    profile = Profile.objects.first()
    pizza = Pizza.objects.get(id=pizza_id)
    context = {
        'pizza': pizza,
        'profile': profile

    }
    return render(request, 'details-pizza.html', context)


def edit_pizza(request, pizza_id):
    profile = Profile.objects.first()
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == "GET":
        context = {'form': CreatePizzaForm(initial=pizza.__dict__)}
        return render(request, 'edit-pizza.html', context)
    else:
        form = CreatePizzaForm(request.POST, instance=pizza)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('dashboard') #po name e tova
        else:
            context = {
                'form': form,
                'profile': profile
            }
            return render(request, 'edit-pizza.html', context)


def delete_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == 'POST':
        pizza.delete()
        return redirect('dashboard')

    form = DeletePizzaForm(instance=pizza)
    context = {'form': form, 'profile': Profile.objects.first()}
    return render(request, 'delete-pizza.html', context)