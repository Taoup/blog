from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postid>/', views.post_details, name='post_detail'),
]