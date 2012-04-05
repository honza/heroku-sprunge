#!/usr/bin/env bash

heroku create --stack cedar
heroku addons:add mongolab:starter

echo "Where will this be hosted?  (no trailing slash, e.g.: http://foo-bar-234.herokuapp.com)"
read SPRUNGE_HOST

heroku config:add "SPRUNGE_HOST=$(echo "$SPRUNGE_HOST" | sed -e 's_/$__')"
heroku config:add "SPRUNGE_MONGO_URI=$(heroku config | grep MONGOLAB_URI | tr -s ' ' | cut -d ' ' -f 3)"
heroku config:add "SPRUNGE_MONGO_DB_NAME=$(heroku config | grep MONGOLAB_URI | sed -e 's_.*/__')"
heroku config:add "SPRUNGE_NAME=sprunge"

git push heroku master
