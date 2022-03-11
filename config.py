
import os

from flask import Config


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    class DevConfig(Config):
     DEBUG = False
