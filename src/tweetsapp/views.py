from django.shortcuts import render, redirect
from django.conf import settings
from twython import Twython, TwythonError


def get_tweeets(request):
    """
    Get latest num tweets from the Twitter user specified as an input.
    """
    if request.is_ajax():
        screen_name = request.GET.get('screen_name', '')
        num_tweets = request.GET.get('num_tweets', '')
        # check if screen name exist and get its time line
        if screen_name and num_tweets:
            TWITTER_USER = screen_name
            twitter = Twython(settings.TWITTER_CONSUMER_KEY,
                              settings.TWITTER_CONSUMER_SECRET,
                              settings.TWITTER_OAUTH_TOKEN,
                              settings.TWITTER_OAUTH_TOKEN_SECRET)
            try:
                user_timeline = twitter.get_user_timeline(screen_name=TWITTER_USER, count=num_tweets)
            except TwythonError as e:
                return {"Exception in get user_timeline ": e}

            result = []
            for tweet in user_timeline:
                result.append(tweet['text'])
            context = {"tweets": result}
        return render(request, "result.html", context)
    else:
        return render(request, "home.html")


def login_twitter(request):
    APP_KEY = settings.TWITTER_CONSUMER_KEY
    APP_SECRET = settings.TWITTER_CONSUMER_SECRET
    twitter = Twython(APP_KEY, APP_SECRET)
    auth = twitter.get_authentication_tokens(callback_url='http://127.0.0.1:8000/callback')
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    request.session['OAUTH_TOKEN_SECRET'] = OAUTH_TOKEN_SECRET
    request.session['OAUTH_TOKEN'] = OAUTH_TOKEN
    return redirect(auth['auth_url'])

def callback(request):
    oauth_verifier = request.GET['oauth_verifier']
    oauth_token = request.GET['oauth_token']
    if 'OAUTH_TOKEN_SECRET' in request.session:
        OAUTH_TOKEN_SECRET = request.session['OAUTH_TOKEN_SECRET']
    twitter = Twython(settings.TWITTER_CONSUMER_KEY,
                      settings.TWITTER_CONSUMER_SECRET,
                      oauth_token,OAUTH_TOKEN_SECRET)
    final_step = twitter.get_authorized_tokens(oauth_verifier)
    #Once you have the final user tokens, store them in a database
    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    twitter = Twython(settings.TWITTER_CONSUMER_KEY,
                  settings.TWITTER_CONSUMER_SECRET,
                  OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    return redirect('get_tweets')