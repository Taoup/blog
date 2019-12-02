from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/<int:tagid>', views.tag_view, name='tags'),
    path('list', views.list_view, name='list'),
    path('post/<int:blogid>', views.post_detail, name='post_detail'),
    path('list/tag/<int:tagid>', views.tagged_list_view, name='tagged_list'),
]