from django.http import JsonResponse
from django.shortcuts import render
import json
import datetime

from Pizza_Django_Framework.accounts.models import PizzaUser
from Pizza_Django_Framework.pizza.models import Pizza
from Pizza_Django_Framework.store.models import Order, OrderItem, ShippingAddress
from .utils import cookieCart, cartData


def store(request):

    if request.user.is_authenticated:
        user = request.user.id
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    #data =cartData(request)
    #cartItems = data['cartItems']
    #order = data['order']
    #items = data['items']

    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas,
        'cartItems': cartItems,
    }
    return render(request, 'store/store.html', context)


def cart(request):
    #data = cartData(request)
    #cartItems = data['cartItems']
    #order = data['order']
    #items = data['items']
    if request.user.is_authenticated:
        user = request.user.id
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }

    return render(request, 'store/cart.html', context)


def checkout(request):
    #data = cartData(request)
    #cartItems = data['cartItems']
    #order = data['order']
    #items = data['items']
    if request.user.is_authenticated:
        user = request.user.id
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }

    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    pizzaId = data['pizzaId']
    action = data['action']

    print('Action:', action)
    print('Pizza:', pizzaId)

    user = request.user.id
    pizza = Pizza.objects.get(id=pizzaId)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, pizza=pizza)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        user = request.user.id
        print(user)
        order, created = Order.objects.get_or_create(user=user, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        # if total == order.get_cart_total:
        #	order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                user_id=user,  # 2 chasa tuk ch da se setq ch e s id
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],

            )
    else:
        print('User is not logged in')

        print('COOKIES:')
    return JsonResponse('Payment complete!', safe=False)
