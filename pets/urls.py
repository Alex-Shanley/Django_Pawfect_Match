from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.list_pets, name='list_pets'),
    path('add/', views.add_pet, name='add_pet'),
    path('edit/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('delete/<int:pet_id>/', views.delete_pet, name='delete_pet'),
]

