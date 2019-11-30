from django.shortcuts import render
from .models import Blogpost, Tag
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import markdown


def _render(request, posts):
    for post in posts:
        post.body = markdown.markdown(post.body,
         extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            ]
        )
    context = {'recent_20_posts': posts}
    return render(request, 'blogpost/index.html', context)


# Create your views here.
def index(request):
    recent_20_posts = Blogpost.objects.order_by('-posted_date')[:20]
    return _render(request, recent_20_posts)


def tag_view(request, tagid):
    # id = get_object_or_404(Tag, name=tagname)
    posts_of_tag = Blogpost.objects.filter(tags=tagid)[:20]
    return _render(request, posts_of_tag)