from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email') 
    list_display_links = ('email', 'first_name', 'last_name')
    filter_horizontal = () 
    list_filter = ()
    fieldsets = () 

admin.site.register(Account, AccountAdmin)