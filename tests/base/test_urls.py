from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Pizza_Django_Framework.pizza.views import home_page,home_details, like_pizza, create_pizza, edit_pizza, delete_pizza, show_pizza_details

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url=reverse('home')
        self.assertEqual(resolve(url).func, home_page)

    #def test_dashboard_url_is_resolved(self):
    #    url=reverse('dashboard')
    #    self.assertEqual(resolve(url).func, home_details())