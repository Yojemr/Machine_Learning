from pathlib import Path
from secrets import token_urlsafe

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = token_urlsafe(48)
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ROOT_URLCONF = 'urls'
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'

MIDDLEWARE = ['django.middleware.csrf.CsrfViewMiddleware']
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
}]
