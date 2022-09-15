wzlk8toolkit_web a web service for kubenetes cluste task management, developed with Django 4.

## Getting started

Before docker-compose build, please add following configurations into the end of
wzlk8toolkit_web/wzlk8toolkit_web/setting.py

```python
import os

DEBUG = False

# don't use this KEY in production
SECRET_KEY = 'vq^_^b++t%wh(xat!xn2tsd+zvg$$=cz7&9sj_gv6zm8d!8@y)'

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wzlk8toolkit_web',
        'USER': 'dbuser',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "foobared",
        },
    }
}
```

and following variables to the wzlk8toolkit_web/.env

```python
MYSQL_ROOT_PASSWORD = 123456
MYSQL_USER = dbuser
MYSQL_DATABASE = wzlk8toolkit_web
MYSQL_PASSWORD = password
```
