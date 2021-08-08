from Posts_App import views
from django.urls import path


app_name= 'Posts_App'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('viewPhoto/', views.viewPhoto, name='viewPhoto'),
    path('add_album/', views.addalbum, name='addalbum'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/',views.unliked, name='unliked'),
]