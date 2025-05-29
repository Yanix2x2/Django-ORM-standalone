import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASES'),
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
