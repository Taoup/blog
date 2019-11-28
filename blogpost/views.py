from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    recent_20_posts = Blogpost.objects.order_by('-posted_date')[:20]
    context = {'recent_20_posts': recent_20_posts}
    return render(request, 'blogpost/index.html', context)

def post_details(request, postid):
    post = Blogpost.objects.filter(pk = postid)
    return HttpResponse(post.get().title)