from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser , BaseUserManager
from decimal import  Decimal  
from django.contrib.auth.hashers import make_password


class Account(models.Model):
      CURRENCY_CHOICES = [('USD', 'Doller'),('IRAN', 'RIALL')]
      
      balance =models.DecimalField(max_digits=30, decimal_places=10 , default=0.00, validators=[MinValueValidator(Decimal('0.00'))])
      balance_currency = models.CharField(
            max_length = 20,
            choices = CURRENCY_CHOICES,
            default = 'USD'
            )
      name = models.CharField(max_length=30, null=True)
      
      def __str__(self) :
                return str(self.balance)

          
class UserManager(models.Manager):

      def regiter_user(self, email, username, password, balance=10.00, first_name="", last_name=""):

            decode_password = make_password(password)
            
            account = Account.objects.create(balance=balance)
            user = self.create(email=email,username=username, password=decode_password )
            user.first_name = first_name
            user.last_name = last_name
            user.account = account
            user.is_staff=True
            user.is_active=True
            user.is_superuser=True
            user.save()
            return True
            # redirect to a new URL
            
      def get_by_natural_key(self, username):
            return self.get(username=username)       
          
class User(AbstractUser):
      account = models.OneToOneField(Account , on_delete=models.CASCADE , null=True)
      objects= UserManager()
      def __str__(self):            
            return self.username
      
      
