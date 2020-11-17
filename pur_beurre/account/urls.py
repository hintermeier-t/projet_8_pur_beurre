from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('', views.connexion, name="connexion")
]

app_name = 'account'