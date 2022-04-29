
from django.test import TestCase

from django.test import SimpleTestCase
from Pizza_Django_Framework.pizza.forms import EditPizzaForm, CreatePizzaForm, DeletePizzaForm
from Pizza_Django_Framework.pizza.models import Pizza
from tests.base.mixins import UserTestUtils
from tests.base.tests import PizzaTestCase


class TestForms(TestCase, UserTestUtils):

    valid_name = 'Test Pizza 1'
    valid_price = 2.0
    valid_image_url = "http://image.com"
    valid_calories = 200
    valid_description = 'Test Description'
    valid_user = "1"

    def test_create_form_valid_data(self):
        form = CreatePizzaForm(data={
            'name': 'Test Pizza',
            'price': 2.0,
            'image_url': 'https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png',
            'calories': 200,
            'description': 'description test'
        })

        self.assertTrue(form.is_valid())

    def test_create_form_no_data(self):
        form = CreatePizzaForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


