import os
basedir = os.path.abspath(os.path.dirname(__file__)) # main application directory

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # This variable takes the location of the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'Your email here'
    MAIL_DEFAULT_SENDER = 'Your email here'
    MAIL_PASSWORD = 'Your email account password here'
    #ADMINS = ['']
    POSTS_PER_PAGE = 5