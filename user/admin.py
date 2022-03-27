from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class MainUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_staff', 'is_student')
    search_fields = ('email', 'username', 'is_student')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,MainUserAdmin)