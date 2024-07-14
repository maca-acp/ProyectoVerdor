from django.urls import path
from . import views

urlpatterns = [
  path('semillas/',views.semillas,name='semillas'),
  path('tierra/',views.tierra,name='tierra'),
  path('herramientas/',views.herramientas,name='herramientas'),
  path('maceteros/',views.maceteros,name='maceteros'),
]