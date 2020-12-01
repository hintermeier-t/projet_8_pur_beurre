from django.urls import path
from django.contrib.auth import logout
from . import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('my_account/', views.my_account, name="my_account"),
    path('save/', views.save, name='save'),
    path('mail_save/', views.mail_save, name='mail_save'),
]

app_name = 'account'