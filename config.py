import os
# from os import path
# if path.exists("env.py"):
#     import env


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    MONGO_URI = os.environ.get('MONGO_URI')
