
from os.path import join

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from Pizza_Django_Framework.accounts.models import Profile
from Pizza_Django_Framework.pizza.models import Pizza

from tests.base.tests import PizzaTestCase


class ProfileDetailsTest(PizzaTestCase):
    def test_getDetails_whenLoggedInUserWithNoPizzas_shouldGetDetailsWithNoPizzas(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['user_pizzas']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInUserWithPizzas_shouldGetDetailsWithPizzas(self):
        pizza = Pizza.objects.create(
            name='Test Pizza',
            description='Test pizza description',
            price=1,
            image_url='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png',
            calories=100,
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([pizza], list(response.context['user_pizzas']))

    def test_postDetails_whenUserLoggedInWithoutImage_shouldChangeImage(self):
        path_to_image = "https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png"


        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        self.assertEqual(path_to_image, profile.profile_image)

    def test_postDetails_whenUserLoggedInWithImage_shouldChangeImage(self):
        path_to_image = 'https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)

