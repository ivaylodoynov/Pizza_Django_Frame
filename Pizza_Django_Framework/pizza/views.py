from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Pizza_Django_Framework.pizza.forms import CreatePizzaForm, DeletePizzaForm, EditPizzaForm
from Pizza_Django_Framework.pizza.models import Pizza, Like
from Pizza_Django_Framework.profiles.models import Profile


def home_page(request):
    #profile = Profile.objects.first()

    pizzas = Pizza.objects.all()

    context = {
        'pizzas': pizzas,
        #'profile': profile,
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

@login_required
def like_pizza(request, pizza_id):
    pizza= Pizza.objects.get(id=pizza_id)
    like_object_by_user = pizza.like_set.filter(user_id = request.user.id).first()

    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            pizza=pizza,
            user=request.user
        )
        like.save()
    return redirect('pizza details', pizza.id)

@login_required
def create_pizza(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = CreatePizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.user = request.user
            pizza.save()
            return redirect('dashboard') #tova e po ime
        context = {'form': form, 'profile': profile}
        return render(request, 'create-pizza.html', context)

    form = CreatePizzaForm()
    context = {'form': form, 'profile': profile}
    return render(request, 'create-pizza.html', context)

@login_required
def show_pizza_details(request, pizza_id):
    profile = Profile.objects.first()
    pizza = Pizza.objects.get(id=pizza_id)
    pizza.likes_count = pizza.like_set.count()

    is_owner = pizza.user == request.user
    superuser = request.user.is_superuser

    is_liked_by_user =pizza.like_set.filter(user_id=request.user.id).exists()

    context = {
        'pizza': pizza,
        'profile': profile,
        'is_owner': is_owner,
        'superuser': superuser,
        'is_liked': is_liked_by_user,

    }
    return render(request, 'details-pizza.html', context)

@login_required
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

@login_required
def delete_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == 'POST':
        pizza.delete()
        return redirect('dashboard')

    form = DeletePizzaForm(instance=pizza)
    context = {'form': form, 'profile': Profile.objects.first()}
    return render(request, 'delete-pizza.html', context)
