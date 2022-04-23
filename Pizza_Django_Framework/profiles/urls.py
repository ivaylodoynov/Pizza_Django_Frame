from django.urls import path
from Pizza_Django_Framework.profiles.views import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = [
    path('details/', show_profile, name='profile'),
    path('create/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]