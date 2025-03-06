from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create_todo, name="create_todo"),
    path('edit/<int:id>', views.update_todo, name="update_todo"),
    path('delete/<int:id>', views.delete_todo, name="delete_todo"),
]