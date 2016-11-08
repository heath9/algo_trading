# setting debug mode
DEBUG = True

# secret_key that need to make CSRF protection
SECRET_KEY = 'this_is_a_secret_key'

# add mongoengine to flask_debugtoolbar view
DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']

# setting flask_debugtoolbar whether intercept redirect
DEBUG_TB_INTERCEPT_REDIRECTS = False

# setting https mode or not
SSL_OR_NOT = True
#SSL_OR_NOT = False

# mongodb database access configuration
MONGODB_SETTINGS = {
    'db': 'trade',
    'host': '192.168.1.150',
    'port': 27017
}
