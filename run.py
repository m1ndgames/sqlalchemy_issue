from apps import create_app
from apps.config import config_dict
from flask_minify import Minify
from sys import exit
from werkzeug.middleware.proxy_fix import ProxyFix

import logging
import os


# WARNING: Don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", False)

# The configuration
if DEBUG:
    get_config_mode = "Debug"
else:
    get_config_mode = "Production"

try:
    # Load the configuration using the default values
    app_config = config_dict[get_config_mode]
except KeyError:
    exit("Error: Invalid <config_mode>. Expected values [Debug, Production] ")

app = create_app(app_config)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)
else:
    Minify(app=app, html=True, js=False, cssless=False)
    logging.basicConfig(level=logging.ERROR)
    app.logger.setLevel(logging.ERROR)
