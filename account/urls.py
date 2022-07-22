from django.urls import path
from django.contrib.auth import views

from .views import registeraccount  
# from . import views
urlpatterns = [
      path('login/', views.LoginView.as_view() , name="login"),
      path('registeraccount/',registeraccount,name="registeraccount"),  
      # path('register/',register ,name="registeraccount")  ,
]
