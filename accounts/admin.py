from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.

# so we add this code to show the fileds an admin panel
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 
                    'last_name', 'username', 'last_login',
                    'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name') # we add this to make it links click on it and we go to the account page
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)