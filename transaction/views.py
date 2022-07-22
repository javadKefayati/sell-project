from django.shortcuts import render
from account.models import User , Account
from .models import Order, Increase_balance
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import  transaction
from .forms import OrderForm ,IncreaseForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
import os

from django.http import JsonResponse
import decimal
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
      """
      View to list all users in the system.

      * Requires token authentication.
      * Only admin users are able to access this view.
      """
      authentication_classes = [authentication.TokenAuthentication]
      permission_classes = [permissions.IsAdminUser]

      def get(self, request, format=None):
            """
            Return a list of all users.
            """
            usernames = [user.username for user in User.objects.all()]
            return Response(usernames)


@login_required   
def log_out(request):
      logout(request)
      return HttpResponseRedirect("/auth/login")

@login_required
def Home(request):
      form = OrderForm ()
      return render(request,"index.html",{'form':form})


@login_required
def registerOrder(request):
      if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                  
                  user_id = request.POST["id"]
                  number = form.cleaned_data["number"]
                  price = decimal.Decimal( form.cleaned_data["price"])
                  
                  status_register_order , message_register_order = Order.objects.register_order(user_id, price,number)

                  if status_register_order:
                        return JsonResponse({"status":1,"message":message_register_order})
                  else :
                        return JsonResponse({"status": 0, "message": message_register_order})
            else : 
                  return JsonResponse({"status": 0, "message": "your info is not correct"})
      
      else :
            return JsonResponse({"status": 0, "message": "your request is not post"})
            
            
@login_required
def Increase(request):
      form = IncreaseForm ()
      return render(request,"increase.html",{"form":form})


@login_required
def registerIncrease(request):                  
      if request.method == "POST":
            form = IncreaseForm(request.POST)
            if form.is_valid():
                  
                  user_id = request.POST["id"]
                  price = form.cleaned_data["price"]
                  
                  status_register_increase , message_register_increase = Increase_balance.objects.register_increase(user_id, price)

                  if status_register_increase:
                        return JsonResponse({"status":1,"message":message_register_increase})
                  else :
                        return JsonResponse({"status": 0, "message": message_register_increase})
            else : 
                  return JsonResponse({"status": 0, "message": "your info is not correct"})
            
      else :
            return JsonResponse({"status": 0, "message": "your request is not post"})

      

def all(request):
      users = User.objects.all().values()
      return JsonResponse({users},safe=False)