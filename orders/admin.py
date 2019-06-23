from django.contrib import admin

# Register your models here.
from .models import Pizza, PizzaPrice, PizzaTopping, Salads, DinnerPlatters, DinnerPlattersPrice, Pasta, Subs, SubsPrice, SubsSteak, SubsSteakPrice
from .models import Order

admin.site.register(Pizza)
admin.site.register(PizzaPrice)
admin.site.register(PizzaTopping)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(DinnerPlattersPrice)
admin.site.register(Pasta)
admin.site.register(Subs)
admin.site.register(SubsPrice)
admin.site.register(SubsSteak)
admin.site.register(SubsSteakPrice)
admin.site.register(Order)
