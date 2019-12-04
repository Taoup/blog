from django.shortcuts import render
from .models import Blogpost, Tag
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, Http404
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
    tags = Tag.objects.all()
    context = {'recent_20_posts': posts, 'tags':tags}
    return render(request, 'blogpost/index.html', context)

def auth_filter(request):
    if request.user.is_authenticated:
        return Blogpost.objects
    else:
        return Blogpost.objects.filter(public=True)

# Create your views here.
def index(request):
    recent_20_posts = auth_filter(request).order_by('-posted_date')[:20]
    return _render(request, recent_20_posts)


def tag_view(request, tagid):
    if tagid >= 2**32:
        raise Http404('Could not found the page')
    valid_id = get_object_or_404(Tag, pk= tagid)
    posts_of_tag = auth_filter(request).filter(tags=valid_id).order_by('-posted_date')[:20]
    return _render(request, posts_of_tag)

def list_view(request):
    all_posts = auth_filter(request).values('posted_date', 'title', 'id').order_by('-posted_date')
    tags = Tag.objects.all()
    return render(request, 'blogpost/list.html', {'posts':all_posts, 'tags':tags})

def tagged_list_view(request, tagid):
    if tagid >= 2**32:
        raise Http404('Could not found the page')
    valid_id = get_object_or_404(Tag, pk= tagid)
    all_posts = auth_filter(request).filter(tags=valid_id).values('posted_date', 'title', 'id').order_by('-posted_date')
    tags = Tag.objects.all()
    return render(request, 'blogpost/list.html', {'posts':all_posts, 'tags':tags})

def post_detail(request, blogid):
    if blogid >= 2**32:
        raise Http404('Could not found the page')
    post = get_object_or_404(auth_filter(request), pk = blogid)
    post.body = markdown.markdown(post.body,
         extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            ]
        )
    tags = Tag.objects.all()
    context = {'post': post, 'tags':tags}
    return render(request, 'blogpost/post_detail.html', context)
