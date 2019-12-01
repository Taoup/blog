from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/<int:tagid>', views.tag_view, name='tags'),
]