from django.contrib import admin
from . import models
from django.utils.html import format_html

@admin.register(models.Order)
class Order_panel(admin.ModelAdmin):
      def delete(self, obj):      
            return format_html('<a class="btn " style="background-color:#a41515;color:white;color:white;padding:7px"  href="/admin/transaction/order/{}/delete/">Delete</a>', obj.id)
      
      delete.allow_tags = True
      delete.short_description = 'Delete order'
      
      list_display = ('id','user_id', 'price','phone_number','delete')

@admin.register(models.Increase_balance)
class increase_base_panel(admin.ModelAdmin):
      
      def delete(self, obj):      
            return format_html('<a class="btn" style="background-color:#a41515;color:white;padding:7px"  href="/admin/transaction/increase_balance/{}/delete/">Delete</a>', obj.id)
      
      delete.allow_tags = True
      delete.short_description = 'Delete increse balance'

      list_display = ('id','user_id', 'price','delete')
      
      
      

