from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('create', views.create),
    path('query/<int:food_start>', views.query),
    path('product/<int:food_id>', views.product),
    path('delete', views.delete),
    path('update', views.update),
    path('search', views.search),
    path('random', views.ran),
    url(r'^$', views.index, name='index')
]