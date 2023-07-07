from django.urls import path

from FuturaApp import views

urlpatterns = [
     path('',views.Index,name='Index'),
     path('coding/<int:id>',views.coding,name='coding'),
     path('non_coding',views.non_coding,name='non_coding'),
     path('contact', views.contact, name='contact'),
     path('diagram', views.diagram, name='diagram'),
 ]