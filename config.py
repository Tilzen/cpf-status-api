from os.path import dirname, abspath, join

basedir = abspath(dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(basedir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SECRET_KEY = 'secretkey'
JWT_SECRET_KEY = 'jwtsecretkey'
