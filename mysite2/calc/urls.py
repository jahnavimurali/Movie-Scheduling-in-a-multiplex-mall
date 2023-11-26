from django.urls import path

from . import views

urlpatterns =[
   path('',views.about, name='about'),
   path('hehe/', views.hehe, name='hehe'),
   path('home/',views.home,name='home'),
   path('first/',views.first,name='first'),
   path('second/',views.second,name='second'),
   path('result/',views.result,name='result')
]