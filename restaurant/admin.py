from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.
from .models import Menu, Booking, Order, MenuItem, Category, OrderItem, Cart

admin.site.register(Menu)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(MenuItem)#need for adding menu items
admin.site.register(Category)#need for making categorys

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)