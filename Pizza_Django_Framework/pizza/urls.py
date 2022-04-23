from django.urls import path
from Pizza_Django_Framework.pizza.views import home_page, home_details, create_pizza, edit_pizza, delete_pizza, \
    show_pizza_details

urlpatterns = [
    path('', home_page, name='home'),
    path('dashboard/', home_details, name='dashboard'),

    path('game/create/', create_pizza, name='create pizza'),
    path('game/edit/<int:pizza_id>/', edit_pizza, name='edit pizza'),
    path('game/delete/<int:pizza_id>/', delete_pizza, name='delete pizza'),
    path('game/details/<int:pizza_id>/', show_pizza_details, name='pizza details'),
]