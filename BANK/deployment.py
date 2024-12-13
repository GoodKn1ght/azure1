import os

from bokeh.colors.named import azure
from django.db import connection

from .settings import *
from .settings import BASE_DIR
from azure.monitor.opentelemetry import configure_azure_monitor


os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"] = "InstrumentationKey=2c52f5a4-668a-43da-b21c-dab5c8c49ccc;IngestionEndpoint=https://polandcentral-0.in.applicationinsights.azure.com/;LiveEndpoint=https://polandcentral.livediagnostics.monitor.azure.com/;ApplicationId=c562c434-d5bb-4ea9-8070-46b0abc01ebb"
configure_azure_monitor()

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATIC_URL = 'static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sys2',
        'HOST': 'centralbank.mysql.database.azure.com',
        'USER': 'centralbank',
        'PASSWORD': 'MYrosyaW1llB3M1ne',
    }
}
