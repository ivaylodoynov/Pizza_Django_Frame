from django.urls import reverse

from Pizza_Django_Framework.pizza.models import Pizza, Like
from tests.base.mixins import UserTestUtils, PizzaTestUtils
from tests.base.tests import PizzaTestCase


class LikePetViewTests(PizzaTestUtils, UserTestUtils, PizzaTestCase):
    def test_likePizza_whenPizzaNotLiked_shouldCreateLike(self):
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


        response = self.client.post(reverse('like pizza', kwargs={
            'pizza_id': pizza.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            pizza_id=pizza.id,
        ) \
            .exists()

        self.assertTrue(like_exists)

    def test_likePizza_whenPizzaAlreadyLiked_shouldDeleteTheLike(self):
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



        response = self.client.post(reverse('like pizza', kwargs={
            'pizza_id': pizza.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            pizza_id=pizza.id,
        ) \
            .exists()

        self.assertFalse(like_exists)