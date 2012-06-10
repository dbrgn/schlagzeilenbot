import sys
import tweepy
import requests
import env
from fabric.api import task


@task
def tweet():
    # Initialize twitter API
    conf = env.prefix('twitter_')
    try:
        auth = tweepy.OAuthHandler(conf['consumer_key'], conf['consumer_secret'])
        auth.set_access_token(conf['access_token'], conf['access_token_secret'])
    except KeyError as e:
        print >> sys.stderr, 'Please provide TWITTER_%s env variable!' % e.message.upper()
        sys.exit(1)
    api = tweepy.API(auth)

    # Get a headline
    headers = {'accept': 'application/json'}
    r = requests.get('http://www.schlagzeilengenerator.ch/', headers=headers)
    headline = r.json['headline']

    # Prepare and send tweet
    template = u'%s http://www.schlagzeilengenerator.ch/'
    available_chars = 140 - len(template % '')
    if len(headline) > available_chars:
        limit = available_chars - 3
        headline = headline[:limit] + '...'
    tweet = unicode(template % headline).encode('utf-8')
    print tweet
    status = api.update_status(tweet)
    print 'https://twitter.com/schlagzeilenbot/status/%s' % status.id_str
