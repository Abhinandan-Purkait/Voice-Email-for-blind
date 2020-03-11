from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('addcontact/', views.addcontact, name='addcontact'),
    path('ajaxForm/', views.ajaxForm, name='ajaxForm')
]
