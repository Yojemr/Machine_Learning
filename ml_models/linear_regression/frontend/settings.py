import os
from pathlib import Path
from secrets import token_urlsafe

BASE_DIR = Path(__file__).resolve().parent
EN_RAILWAY = bool(os.environ.get('RAILWAY_ENVIRONMENT_ID'))
ESTIMADOR_INTEGRADO = os.environ.get('ESTIMADOR_INTEGRADO') == '1'
DOMINIO_PUBLICO = os.environ.get('RAILWAY_PUBLIC_DOMAIN')

DEBUG = not EN_RAILWAY
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
if DOMINIO_PUBLICO:
    ALLOWED_HOSTS.append(DOMINIO_PUBLICO)

if EN_RAILWAY:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    CSRF_COOKIE_SECURE = True
else:
    SECRET_KEY = token_urlsafe(48)

if ESTIMADOR_INTEGRADO:
    SWAGGER_URL = '/docs'
else:
    BACKEND_URL = (
        os.environ['BACKEND_URL'] if EN_RAILWAY
        else os.environ.get('BACKEND_URL', 'http://127.0.0.1:8000')
    ).rstrip('/')
    SWAGGER_URL = f'{BACKEND_URL}/docs'

ROOT_URLCONF = 'urls'
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
}]
