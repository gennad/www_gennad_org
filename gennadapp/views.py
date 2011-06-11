from django.shortcuts import render_to_response
from django.template import loader
from django.template import Context, RequestContext
from django.http import HttpResponse
from models import BlogPost

def index(request):
  return render_to_response(
    'index.html',
    context_instance = RequestContext(request)
  )

def archive(request):
  posts = BlogPost.objects.all()
  t = loader.get_template('archive.html')
  c = Context( {'posts': posts })
  return HttpResponse(t.render(c))
