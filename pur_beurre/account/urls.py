from django.urls import path
from django.contrib.auth import logout
from . import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('my_account/', views.my_account, name="my_account")
]

app_name = 'account'