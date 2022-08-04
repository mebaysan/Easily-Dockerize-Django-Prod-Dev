# If you want to use this config file, you should set `DEBUG=True` on your terminal

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "verySECRETk3y"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
}
