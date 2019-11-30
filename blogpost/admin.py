from django.contrib import admin
from blogpost.models import Blogpost, Tag

# Register your models here.

class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']

admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Tag)