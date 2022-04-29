from django.core.exceptions import ValidationError
from django.test import TestCase

from django.test import SimpleTestCase
from Pizza_Django_Framework.pizza.models import Pizza
from tests.base.mixins import UserTestUtils


class TestPizzaModels(TestCase, UserTestUtils):

    valid_name = 'Test Pizza 1'
    valid_price = 2.0
    valid_image_url = "http://image.com"
    valid_calories = 200
    valid_description = 'Test Description'
    valid_user = "1"

    def test_model_when_name_is_longer_than_30_characters(self):
        name = "Test Test Test Test Test Test Test Test Test"
        pizza_user = self.create_user(email='pizza@user.com', password='123456')

        pizza = Pizza(
            name = name,
            price = self.valid_price,
            image_url = self.valid_image_url,
            calories = self.valid_calories,
            description=self.valid_description,
            user = pizza_user
        )

        with self.assertRaises(ValidationError) as context:
            pizza.full_clean()
            pizza.save()

        self.assertIsNotNone(context.exception)

    def test_model_when_price_is_lower_than_0(self):
        price = -1
        pizza_user = self.create_user(email='pizza@user.com', password='123456')


        pizza = Pizza(
            name=self.valid_name,
            price=price,
            image_url=self.valid_image_url,
            calories=self.valid_calories,
            description=self.valid_description,
            user = pizza_user
        )

        with self.assertRaises(ValidationError) as context:
            pizza.full_clean()
            pizza.save()

        self.assertIsNotNone(context.exception)

    def test_model_when_price_is_0_success(self):
        price = 0
        pizza_user = self.create_user(email='pizza@user.com', password='123456')


        pizza = Pizza(
            name=self.valid_name,
            price=price,
            image_url=self.valid_image_url,
            calories=self.valid_calories,
            description=self.valid_description,
            user = pizza_user
        )

        pizza.full_clean()
        pizza.save()

    def test_model_when_invalid_url(self):
        image_url = 'http'
        pizza_user = self.create_user(email='pizza@user.com', password='123456')

        pizza = Pizza(
            name=self.valid_name,
            price=self.valid_price,
            image_url=image_url,
            calories=self.valid_calories,
            description=self.valid_description,
            user=pizza_user
        )

        with self.assertRaises(ValidationError) as context:
            pizza.full_clean()
            pizza.save()

        self.assertIsNotNone(context.exception)

    def test_model_when_calories_is_lower_than_1(self):
        calories = 0
        pizza_user = self.create_user(email='pizza@user.com', password='123456')

        pizza = Pizza(
            name=self.valid_name,
            price=self.valid_price,
            image_url=self.valid_image_url,
            calories=calories,
            description=self.valid_description,
            user=pizza_user
        )

        with self.assertRaises(ValidationError) as context:
            pizza.full_clean()
            pizza.save()

        self.assertIsNotNone(context.exception)

    def test_model_when_calories_is_1_success(self):
        calories = 1
        pizza_user = self.create_user(email='pizza@user.com', password='123456')

        pizza = Pizza(
            name=self.valid_name,
            price=self.valid_price,
            image_url=self.valid_image_url,
            calories=calories,
            description=self.valid_description,
            user=pizza_user
        )

        pizza.full_clean()
        pizza.save()

    def test_model_when_description_is_populated(self):
        description = "Test description"
        pizza_user = self.create_user(email='pizza@user.com', password='123456')

        pizza = Pizza(
            name=self.valid_name,
            price=self.valid_price,
            image_url=self.valid_image_url,
            calories=self.valid_calories,
            description=description,
            user=pizza_user
        )

        pizza.full_clean()
        pizza.save()

    def test_model_when_description_is_blank(self):
        description = ""
        pizza_user = self.create_user(email='pizza@user.com', password='123456')

        pizza = Pizza(
            name=self.valid_name,
            price=self.valid_price,
            image_url=self.valid_image_url,
            calories=self.valid_calories,
            description=description,
            user=pizza_user
        )

        pizza.full_clean()
        pizza.save()


        #name = models.CharField(max_length=30)
        #price = models.FloatField(validators=[MinValueValidator(0)])
        #image_url = models.URLField()
        #calories = models.IntegerField(validators=[MinValueValidator(1)])
        #description = models.TextField(null=True, blank=True)