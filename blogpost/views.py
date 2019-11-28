from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse
from django.shortcuts import render
import markdown


# Create your views here.
def index(request):
    recent_20_posts = Blogpost.objects.order_by('-posted_date')[:20]
    for post in recent_20_posts:
        post.body = markdown.markdown(post.body,
         extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            ]
        )
    context = {'recent_20_posts': recent_20_posts}
    return render(request, 'blogpost/index.html', context)
