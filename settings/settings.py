#  Rest of the settings.py can be changed for projects. For my set-up, I need the lines below.
import os
from distutils.util import strtobool
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = bool(strtobool(os.getenv("DEBUG")))
if DEBUG == True:
    from .config_dev import *
else:
    from .config_prod import *
