
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pizza_Django_Framework.pizza.urls')),
    path('profiles/', include('Pizza_Django_Framework.profiles.urls')),
    path('accounts/', include('Pizza_Django_Framework.accounts.urls')),
    path('store/', include('Pizza_Django_Framework.store.urls')),
]
