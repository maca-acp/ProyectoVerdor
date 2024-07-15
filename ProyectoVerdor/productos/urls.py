from django.urls import path,include
from . import views

urlpatterns = [
  path('semillas/',views.semillas,name='semillas'),
  path('tierra/',views.tierra,name='tierra'),
  path('herramientas/',views.herramientas,name='herramientas'),
  path('maceteros/',views.maceteros,name='maceteros'),
  path('save_cart/',views.save_cart, name='save_cart'),
  path('inicio/',views.inicio,name='inicio'),
  path('login/', views.login, name='login'),
  path("accounts/", include("django.contrib.auth.urls")),
  path('usuarios_listar/', views.crud, name='usuarios_listar'),
  path('registro/', views.registro, name='registro'),
  path('home', views.home, name='home'),
  path("accounts/", include("django.contrib.auth.urls")),
]