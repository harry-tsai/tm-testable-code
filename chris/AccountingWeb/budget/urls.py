from django.urls import path

from . import views

urlpatterns = [
    path('', views.budget, name='budget'),
    path('budget_create', views.budget_create, name='budget_create')    
]
