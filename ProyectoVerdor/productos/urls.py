from django.urls import path
from . import views

urlpatterns = [
  path('semillas/',views.semillas,name='semillas'),
  path('tierra/',views.tierra,name='tierra'),
  path('herramientas/',views.herramientas,name='herramientas'),
  path('maceteros/',views.maceteros,name='maceteros'),
  path('save_cart/',views.save_cart, name='save_cart'),
  path('inicio/',views.inicio,name='inicio')
]