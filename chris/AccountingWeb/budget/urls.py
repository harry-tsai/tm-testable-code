from django.urls import path

from . import views

urlpatterns = [
    path('', views.budget, name='budget'),
    path('budget_create', views.budget_create, name='budget_create'),
    path('budget_query', views.budget_query, name='budget_query'),
    path('budget_query_result', views.budget_query_result, name='budget_query_result'),    
]
