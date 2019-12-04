from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Blogpost(models.Model):

    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted_date = models.DateField(db_index=True, auto_now_add=True)

    tags = models.ManyToManyField(Tag, blank=True)
    public = models.BooleanField(default = True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title




