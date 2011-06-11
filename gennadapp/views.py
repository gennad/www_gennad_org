from django.shortcuts import render_to_response
from django.template import loader
from django.template import Context, RequestContext
from django.http import HttpResponse
from models import BlogPost, Client_Twitter

from django.conf import settings

import urlparse

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


import oauth2 as oauth

def twitter_connect(request):
    from utils import pdb; pdb()
    twitter_consumer_key = settings.TWITTER_CONSUMER_KEY
    twitter_consumer_secret = settings.TWITTER_CONSUMER_SECRET

    request_token_url = 'http://twitter.com/oauth/request_token'
    access_token_url = 'http://twitter.com/oauth/access_token'
    authorize_url = 'http://twitter.com/oauth/authorize'
    consumer = oauth.Consumer(twitter_consumer_key,twitter_consumer_secret)

    try:
        next = '/dashboard/'
        if('redirect' in request.session):
            next = request.session['redirect']
            del request.session['redirect']
        twitter = Client_Twitter.objects.get(user=request.user.get_profile())
        return HttpResponseRedirect(next)
        #return HttpResponseRedirect('/account/login?next='+next)
    except: pass

    if ('oauth_verifier' not in request.GET):
        client = oauth.Client(consumer)
        resp, content = client.request(request_token_url, "GET")
        request_token = dict(urlparse.parse_qsl(content))
        roauth_token = request_token['oauth_token']
        roauth_token_secret = request_token['oauth_token_secret']
        request.session['roauth_token'] = roauth_token
        request.session['roauth_token_secret'] = roauth_token_secret
        new_authorize_url = authorize_url+'?oauth_token='+request_token['oauth_token']
        return HttpResponseRedirect(new_authorize_url)

    elif(request.GET['oauth_verifier'] != "" ):
        oauth_verifier = request.GET['oauth_verifier']
        token = oauth.Token(request.session.get('roauth_token', None),request.session.get('roauth_token_secret', None))
        token.set_verifier(oauth_verifier)
        client = oauth.Client(consumer, token)


        resp, content = client.request(access_token_url, "POST")
        access_token = dict(urlparse.parse_qsl(content))


        del request.session['roauth_token']
        del request.session['roauth_token_secret']

        oauth_token = access_token['oauth_token']
        oauth_token_secret = access_token['oauth_token_secret']
        userid = access_token['user_id']
        screenname = access_token['screen_name']


    twitter_user = Client_Twitter.objects.get(user = client)
    access_token = twitter_user.access_token
    access_token_secret = twitter_user.access_token_secret
    token = oauth.Token(access_token,access_token_secret)
    consumer_key = settings.TWITTER_CONSUMER_KEY
    consumer_secret = settings.TWITTER_CONSUMER_SECRET
    consumer = oauth.Consumer(consumer_key,consumer_secret)
    client = oauth.Client(consumer,token)

    data = {'status':'I just checked at 24 hr Fitness'}
    request_uri = 'https://api.twitter.com/1/statuses/update.json'
    resp, content = client.request(request_uri, 'POST', urllib.urlencode(data))


