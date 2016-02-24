from django.shortcuts import render
from django.conf import settings
from twython import Twython, TwythonError


def get_tweeets(request):
    """
    Get latest five tweets from the Twitter user specified as an input.
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
