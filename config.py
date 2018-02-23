# Status debug okruzenja
DEBUG = True

# Definisi glavni direktorijum aplikacije
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Podesavanje baze podataka
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/BAZA'
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Threads
THREADS_PER_PAGE = 2

# Omoguci zastitu od CSRF
CSRF_ENABLED     = True
CSRF_SESSION_KEY = ''

# Kljuc za enkriptovanje kolacica
SECRET_KEY = ''

# Log fajl
LOG_FILE = 'app.log'

# Sessions
SESSION_TYPE = 'sqlalchemy'