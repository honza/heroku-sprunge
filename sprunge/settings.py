import os
import sys


def get_value(key):
    try:
        return os.environ['SPRUNGE_%s' % key]
    except KeyError:
        print 'Env error: %s is not set.' % key
        sys.exit(1)



HOST = get_value('HOST')
NAME = get_value('NAME')  # the POST payload key
MONGO_URI = get_value('MONGOLAB_URI')
MONGO_DB_NAME = get_value('MONGO_DB_NAME')
