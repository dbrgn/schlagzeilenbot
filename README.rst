###############
schlagzeilenbot
###############

Regularly tweet headlines from schlagzeilengenerator.ch.

https://twitter.com/schlagzeilenbot


Setup (Heroku)
==============

::

    $ heroku apps:create [appname]
    $ heroku addons:add scheduler:standard
    $ heroku config:add TWITTER_ACCESS_TOKEN=[value]
    $ heroku config:add TWITTER_ACCESS_TOKEN_SECRET=[value]
    $ heroku config:add TWITTER_CONSUMER_KEY=[value]
    $ heroku config:add TWITTER_CONSUMER_SECRET=[value]
    $ git push heroku master


Authors
=======

* Danilo Bargen (Github: `@dbrgn <https://github.com/dbrgn/>`_, Twitter: `@dbrgn <https://twitter.com/dbrgn>`_)
