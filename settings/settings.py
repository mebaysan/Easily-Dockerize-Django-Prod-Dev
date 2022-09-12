#  Rest of the settings.py can be changed for projects. For my set-up, I need the lines below.
# Do not forget to remove default DATABAES variable to prevent database duplication!!!!
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = int(os.environ.get("DEBUG", default=0))
if DEBUG == 1:
    from .config_dev import *
else:
    from .config_prod import *
