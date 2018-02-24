from flask import Flask, render_template
from werkzeug.contrib.cache import SimpleCache

# Import Session
from flask_session import Session

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Logging
import logging
from logging.handlers import RotatingFileHandler

# WSGI
app = Flask(__name__)

# Ucitaj konfiguracije iz fajla config.py
app.config.from_object('config_local')

# Session
Session(app)

# Logovanje
handler = RotatingFileHandler(app.config['LOG_FILE'], maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
logger = app.logger

# Baza podataka
db = SQLAlchemy(app)

# SimpleCache
cache = SimpleCache()

# Stranica za gresku 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Importuj module
from app.mod_home.controllers import mod_home as home_module

# Registruj module
app.register_blueprint(home_module)

# Napravi bazu podataka
db.create_all()