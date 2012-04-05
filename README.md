heroku sprunge
==============

*Roll your own sprunge on your domain*

This is inspired by and shares some code with http://sprunge.us.

This is a simple Flask app that uses Pygments to highlight the code.  It uses
MongoDB to store the snippets.  Heroku gives you 240MB of MongoDB storage for
free.  All you need is a free Heroku account and a bit of time.


Setup
-----

Make sure you've got Heroku's command line utility installed and configured
first.

    $ git clone git://github.com/honza/heroku-sprunge.git
    $ cd heroku-sprunge
    $ ./bootstrap.sh

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
