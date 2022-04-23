from django.urls import path
from Pizza_Django_Framework.profiles.views import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = [
    path('profile/details/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]