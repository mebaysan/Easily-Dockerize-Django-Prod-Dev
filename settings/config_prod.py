# Values are coming from docker-compose.yml
import os

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

CORS_ALLOWED_ORIGINS = []

CSRF_TRUSTED_ORIGINS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
    }
}


# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True


LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {"format": "%(levelname)s %(asctime)s %(name)s %(message)s"},
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": "/var/log/rmore/debug.log",
            },
        },
        "loggers": {
            "django_auth_adfs": {
                "handlers": ["console"],
                "level": "DEBUG",
            },
            "django": {
                "handlers": ["file"],
                "level": "DEBUG",
                "propagate": True,
            },
        },
    }