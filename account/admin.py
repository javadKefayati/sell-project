from csv import list_dialects
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , Account
from django.utils.html import format_html
# Register your models here.

UserAdmin.list_display += ('id', 'account')
UserAdmin.fieldsets[1][1]["fields"]=(
       ('first_name', 'last_name', 'email',"account")
      
)
class AccountAdmin(admin.ModelAdmin):
       list_display = ["id","name","balance","balance_currency"]

admin.site.register(User,UserAdmin)

admin.site.register(Account,AccountAdmin)