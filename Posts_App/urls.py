from Posts_App import views
from django.urls import path
from .views import Home

app_name= 'Posts_App'

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('album/', views.album_show, name='album_show'),
    path('add_album/', views.add_album, name='add_album'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/',views.unliked, name='unliked'),
]