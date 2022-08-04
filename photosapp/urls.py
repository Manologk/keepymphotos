from django.urls import path
from photosapp import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('addphoto/', views.addPhoto, name='addphoto'),
    path('photo/<str:pk>/', views.viewphoto, name='viewphoto'),
]