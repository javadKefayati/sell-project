from django.shortcuts import render ,HttpResponse 
from django.http import JsonResponse
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import 
from .models import User 
from .forms import registerForm
from django.contrib.auth.hashers import make_password
from django.db import  transaction

# # from .forms  import AccountForm

# Create your views here.

def logIn(request):
     return render(request,"logIn.html")
      
      
def registeraccount(request):
     # if this is a POST request we need to process the form data
    
     if request.method == 'POST':
          # create a form instance and populate it with data from the request:
          register_form = registerForm(request.POST)
          
          if register_form.is_valid():
               # process the data in form.cleaned_data as required
               first_name = form.cleaned_data["name"]
               last_name = form.cleaned_data["family"]
               email = form.cleaned_data["email"]
               username = form.cleaned_data["username"]
               password =  form.cleaned_data["password"]

               # check whether it's valid:
               if   User.objects.regiter_user(first_name,last_name,email,username,password) :
               
                    return HttpResponseRedirect('/auth/login')
               else:
                    return render(request, 'registration/registeraccount.html', {'form': register_form})
          else :
               return render(request, 'registration/registeraccount.html', {'form': register_form})
               

     # if a GET (or any other method) we'll create a blank form
     else:
          form = registerForm()
          # return JsonResponse(list(form.fields),safe=False)
          return render(request, 'registration/registeraccount.html', {'form': form})

