from django.urls import path

from . import views


urlpatterns = [
    path('search/', views.search,name="search"),
    path('', views.results, name="results"),
    path('<int:product_id>/', views.detail,name="detail"),
]

app_name = 'catalog'