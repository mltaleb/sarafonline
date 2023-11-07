#default config
import os
from dotenv import load_dotenv
load_dotenv()

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my secretkey here is the secret key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
        )

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    WTF_CSRF_ENABLED = False
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class ConfigCapatcha():
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY= os.environ.get('RECAPTCHA_PRIVATE_KEY')
class stripeconfig():
    STRIPE_PUBLIC_KEY= os.environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY= os.environ.get('STRIPE_PUBLIC_KEY')