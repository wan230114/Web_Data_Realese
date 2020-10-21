"""
This is an example settings/test.py file.
Use this settings file when running tests.
These settings overrides what's in settings/base.py
"""

from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

SECRET_KEY = 'x4vk2^7!jap4wm+1pd!6^a6r+%8(es@(t%r9&71^ek(4x8ffu#'
