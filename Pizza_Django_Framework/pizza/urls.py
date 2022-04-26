from django.urls import path
from Pizza_Django_Framework.pizza.views import home_page, home_details, create_pizza, edit_pizza, delete_pizza, \
    show_pizza_details, like_pizza

urlpatterns = [
    path('', home_page, name='home'),
    path('dashboard/', home_details, name='dashboard'),

    path('pizza/create/', create_pizza, name='create pizza'),
    path('pizza/edit/<int:pizza_id>/', edit_pizza, name='edit pizza'),
    path('pizza/delete/<int:pizza_id>/', delete_pizza, name='delete pizza'),
    path('pizza/like/<int:pizza_id>', like_pizza, name='like pizza'),
    path('pizza/details/<int:pizza_id>/', show_pizza_details, name='pizza details'),
]