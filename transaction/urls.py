from django.urls import path
from . import views
urlpatterns = [
    path("logout/",views.log_out),
    path("home/",views.Home),
    path("increase/",views.Increase),
    path("increase/register/",views.registerIncrease),
    path("home/registerorder/",views.registerOrder),
    path("all",views.all),
]
