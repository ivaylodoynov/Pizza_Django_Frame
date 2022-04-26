from django.contrib import admin

from Pizza_Django_Framework.pizza.models import Pizza


class PizzaInlineAdmin(admin.StackedInline):
    model = Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')