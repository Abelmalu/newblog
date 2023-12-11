
from django.contrib import admin
from django.urls import path, include
from . import views

app_name='articles'
urlpatterns = [
    path('', views.artcile_list, name="list"),
    path('create/', views.artcile_create, name="create"),
    path('<slug:slug>/', views.article_detail, name='detail'),
   

]
