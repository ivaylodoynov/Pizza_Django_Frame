from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from tests.base.mixins import UserTestUtils, PizzaTestUtils
from tests.base.tests import PizzaTestCase


class PizzaTests(PizzaTestCase, UserTestUtils, PizzaTestUtils):
    @patch('Pizza_Django_Framework.pizza.models.Pizza.objects')
    def test_Home_View(self, pizza_mock):
        pizza_mock.all.return_value =[1]
        client = Client()
        response = client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home-page.html')

    @patch('Pizza_Django_Framework.pizza.models.Pizza.objects')
    def test_Dashboard_View_No_Profile(self, pizza_mock):
        pizza_mock.all.return_value =[1]
        client = Client()
        response = client.get(reverse('login user'))
        self.assertTemplateUsed(response, 'accounts/login.html')


    @patch('Pizza_Django_Framework.pizza.models.Pizza.objects')
    def test_Create_View_No_Profile(self, pizza_mock):
        self.client.force_login(self.user)
        pizza_mock.all.return_value = [1]
        client = Client()
        response = client.get(reverse('login user'))
        self.assertTemplateUsed(response, 'accounts/login.html')

    @patch('Pizza_Django_Framework.pizza.models.Pizza.objects')
    def test_Create_View_with_Profile(self, pizza_mock):
        self.client.force_login(self.user)
        pizza_mock.all.return_value = [1]
        response = self.client.get(reverse('create pizza'))
        self.assertTemplateUsed(response, 'create-pizza.html')

    @patch('Pizza_Django_Framework.pizza.models.Pizza.objects')
    def test_Edit_View_No_Profile(self, pizza_mock):
        self.client.force_login(self.user)
        pizza_mock.all.return_value = [1]
        client = Client()
        response = client.get(reverse('login user'))
        self.assertTemplateUsed(response, 'accounts/login.html')

    #@patch('Pizza_Django_Framework.pizza.models.Pizza.objects')
    def test_Delete_View_with_Profile(self):
        pizza_user = self.create_user(email='pizza@user.com', password='123456')
        pizza = self.create_pizza(
            name='Test Pizza',
            description='Test pizza description',
            price=1,
            image_url='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png',
            calories=100,
            user=pizza_user,
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete pizza', kwargs={
            'pizza_id': pizza.id,
        }))

        self.assertTrue(response.context['form'])

    def test_Edit_View_with_Profile(self):
        pizza_user = self.create_user(email='pizza@user.com', password='123456')
        pizza = self.create_pizza(
            name='Test Pizza',
            description='Test pizza description',
            price=1,
            image_url='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png',
            calories=100,
            user=pizza_user,
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit pizza', kwargs={
            'pizza_id': pizza.id,
        }))

        self.assertTrue(response.context['form'])