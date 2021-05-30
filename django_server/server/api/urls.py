from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('create', views.create),
    path('query/<int:food_start>', views.query),
    path('product/<int:food_id>', views.product),
    path('delete', views.delete),
    path('update', views.update),
    path('search', views.search)
]