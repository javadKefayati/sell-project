from django.db import models
from djmoney.models.fields import MoneyField
from account.models import User , Account
from django.core.validators import MinValueValidator
from decimal import  Decimal
from django.db import  transaction
from .forms import OrderForm ,IncreaseForm
from math import fsum

from django.http import JsonResponse

# Create your models here.
@transaction.atomic
class OrderManager(models.Manager):
      
      def register_order(self, user_id  , price , number , is_username=True):
                              
            if is_username:
                  user = User.objects.get(username=user_id)
            else:
                  user = User.objects.get(id=user_id)
            
            account_of_user = Account.objects.get( id = user.account_id)
                  
            try:
                  point = transaction.savepoint()

                  order = self.create(
                        user_id=user, phone_number=number, price=price)
                  order.save()
                  
                  if account_of_user.balance-price  >0:
                        account_of_user.balance -= Decimal( price)
                        account_of_user.save(update_fields=['balance'])
                        transaction.savepoint_commit(point)
                        return True , "" , account_of_user.balance
                  else: 
                        transaction.savepoint_rollback(point)
                        return False, "You have not enogh balance" , account_of_user.balance
                  
            except Exception as e:
                  transaction.savepoint_rollback(point)
                  return False ,"Error" , account_of_user.balance
            


class Order(models.Model):
      user_id = models.ForeignKey(User, on_delete=models.CASCADE)
      price  = models.DecimalField(max_digits=30, decimal_places=10 ,validators=[MinValueValidator(Decimal('0.00'))])
      phone_number = models.CharField(max_length=14)
      objects = OrderManager()
      
      
class Increase_balance_manager(models.Manager):
      
      @transaction.atomic
      def register_increase(self, user_id , price , is_username=True):

            if is_username:
                        user = User.objects.get(username=user_id)
            else:
                  user = User.objects.get(id=user_id)
                  
            account_of_user = Account.objects.get( id = user.account_id)
            
            try:
                  #save this point of transaction
                  point = transaction.savepoint()

                  increase = self.create(user_id=user , price=price)
                  increase.save()

                  if price >0 :
                        account_of_user.balance = fsum( [Decimal(price) , account_of_user.balance ])
                        account_of_user.save(update_fields=['balance'])

                  transaction.savepoint_commit(point)
                  return True , "" ,account_of_user.balance
            
            except Exception as e:
                  transaction.savepoint_rollback(point)
                  return False, "Error", account_of_user.balance


class Increase_balance(models.Model):
      user_id = models.ForeignKey(User, on_delete=models.CASCADE)
      price  = models.DecimalField(max_digits=30, decimal_places=10 ,validators=[MinValueValidator(Decimal('0.00'))])
      objects = Increase_balance_manager()
      
      

