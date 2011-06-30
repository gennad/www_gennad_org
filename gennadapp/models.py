from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=150)

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    categories = models.ManyToManyField('Category')
    class Meta:
        ordering = ('-timestamp',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)

class Client_Twitter(models.Model):
    user = models.OneToOneField('Client')
    twitter_id = models.DecimalField(max_digits=20, decimal_places=0,null=True)
    access_token = models.CharField(max_length=200,null=True)
    access_token_secret = models.CharField(max_length=200,null=True)
    twitter_username = models.CharField(max_length=200,null=True)
    def __unicode__(self):
        return self.user.user.username
