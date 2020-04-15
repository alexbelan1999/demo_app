from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('cylinder/', views.cylinder),
    path('paral/', views.paral),
    path('admin/', admin.site.urls),
]
