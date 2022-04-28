from django.urls import reverse

from Pizza_Django_Framework.pizza.models import Pizza, Like
from tests.base.mixins import UserTestUtils, PizzaTestUtils
from tests.base.tests import PizzaTestCase


class PizzaDetailsTest(PizzaTestUtils, UserTestUtils, PizzaTestCase):
    def test_getPizzaDetails_whenPizzaDoesNotExistsAndIsOwner_shouldReturnDetailsForOwner(self):
        pass

    def test_getPizzaDetails_whenPizzaExistsAndIsOwner_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        pizza = self.create_pizza(
            name='Test Pizza',
            description='Test pizza description',
            price=1,
            image_url='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png',
            calories=100,
            user=self.user,
        )

        response = self.client.get(reverse('pizza details', kwargs={
            'pizza_id': pizza.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPizzaDetails_whenPizzaExistsAndIsNotOwnerAndNotLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        pizza_user = self.create_user(email='pizza@user.com', password='123456')
        pizza = self.create_pizza(
            name='Test Pizza',
            description='Test pizza description',
            price=1,
            image_url='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png',
            calories=100,
            user=pizza_user,
        )

        response = self.client.get(reverse('pizza details', kwargs={
            'pizza_id': pizza.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPizzaDetails_whenPizzaExistsAndIsNotOwnerAndLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        pizza_user = self.create_user(email='pizza@user.com', password='123456')
        pizza = self.create_pizza_with_like(
            like_user=self.user,
            name='Test Pizza',
            description='Test pizza description',
            price=1,
            image_url='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png',
            calories=100,
            user=pizza_user,
        )

        response = self.client.get(reverse('pizza details', kwargs={
            'pizza_id': pizza.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])