from django import forms
from django.core.validators import MinValueValidator
from decimal import  Decimal

class OrderForm(forms.Form):      
      number = forms.RegexField(label=("My Label"), max_length=11 ,min_length=11, regex=r'^09[0-9]+$')
      price = forms.DecimalField(label='price',required=True ,validators=[MinValueValidator(Decimal('0.00'))])
      

class IncreaseForm(forms.Form):      
      price = forms.DecimalField(label='price',required=True,validators=[MinValueValidator(Decimal('0.00'))])
      


    
      