heroku sprunge
==============

*Roll your own sprunge on your domain*

This is inspired by and shares some code with http://sprunge.us.

This is a simple Flask app that uses Pygments to highlight the code.  It uses
MongoDB to store the snippets.  Heroku gives you 240MB of MongoDB storage for
free.  All you need is a free Heroku account and a bit of time.


Setup
-----

    $ git clone git://github.com/honza/heroku-sprunge.git
    $ cd heroku-sprunge
    $ heroku create --stack cedar
    $ heroku addons:add mongolab:starter
    $ # Add settings: heroku config:add 
    $ git push heroku master

Env settings
------------

* `SPRUNGE_HOST` - the url where this will be hosted (no trailing slash)
* `SPRUNGE_NAME` - the POST payload key
* `SPRUNGE_MONGO_URI` - the MongoLab URL from Heroku (`heroku config | grep
  mongo`)
* `SPRUNGE_MONGO_DB_NAME` - the string after the last slash on
  `SPRUNGE_MONGO_URI`
* `SPRUNGE_STYLE` - Pygments style (defaults to `default`)


Set these with:

    $ heroku config:add KEY=VALUE

Hacking
-------

Modify the `run.sh` file with your settings and use it to run the app locally.

Example
-------

Here is an example of the app running on Heroku:

http://quiet-sky-4922.herokuapp.com/

License
-------

BSD, short and sweet.
