from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import FoodItem, OrderItem, Order



# Register your models here.

class FoodDisplay(admin.ModelAdmin):
    list_display = ('name','price','availability','description')
    search_fields = ('name','price','availability')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class OrderDisplay(admin.ModelAdmin):
    list_display = ('customer','date_ordered','total')
    search_fields = ('customer','order_items')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(FoodItem,FoodDisplay)
admin.site.register(OrderItem)
admin.site.register(Order,OrderDisplay)
