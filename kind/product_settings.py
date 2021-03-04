
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_NAME = os.environ.get('DATA_NAME')
DATA_USER = os.environ.get('DATA_USER')
DATA_PASSWORD = os.environ.get('DATA_PASSWORD')
DATA_HOST = os.environ.get('DATA_HOST')
DATA_PORT = os.environ.get('DATA_PORT')
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'h4t59z14nb2*3a8fmph(-k0snl=n$)9ceb@*a@jm)@nv+9cd=t')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATA_NAME ,
        'USER' : DATA_USER,
        'PASSWORD' : DATA_PASSWORD,
        'HOST' : DATA_HOST,
        'PORT': DATA_PORT,
    }
}





STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
