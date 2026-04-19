from django.urls import path
from . import views

urlpatterns = [
    path('', views.personnel_list, name='personnel_list'),
    path('add/', views.personnel_create, name='personnel_create'),
    path('edit/<int:pk>/', views.personnel_update, name='personnel_update'),
    path('delete/<int:pk>/', views.personnel_delete, name='personnel_delete'),
]