from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap


apple = Flask(__name__)
apple.config.from_object(Config)
db = SQLAlchemy(apple) #object that represents the database
migrate = Migrate(apple, db) #migration engine
login = LoginManager(apple)
login.login_view = 'login'
mail = Mail(apple)
bootstrap = Bootstrap(apple)

if not apple.debug:
    if apple.config['MAIL_SERVER']:
        auth = None
        if apple.config['MAIL_USERNAME'] or apple.config['MAIL_PASSWORD']:
            auth = (apple.config['MAIL_USERNAME'], apple.config['MAIL_PASSWORD'])
        secure = None
        if apple.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(apple.config['MAIL_SERVER'], apple.config['MAIL_PORT']),
            fromaddr='no-reply@' + apple.config['MAIL_SERVER'],
            toaddrs=apple.config['ADMINS'], subject='Myblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        apple.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/myblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    apple.logger.addHandler(file_handler)

    apple.logger.setLevel(logging.INFO)
    apple.logger.info('Myblog startup')

from blog import routes, models, errors