
from django.contrib.auth import get_user_model

from Pizza_Django_Framework.pizza.models import Pizza, Like

UserModel = get_user_model()


class PizzaTestUtils:
    def create_pizza(self, **kwargs):
        return Pizza.objects.create(**kwargs)

    def create_pizza_with_like(self, like_user, **kwargs):
        pizza = self.create_pizza(**kwargs)
        Like.objects.create(
            pizza=pizza,
            user=like_user,
        )
        return pizza


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)