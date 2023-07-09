# Copy this file to local_settings.py and fill in the required information.
# The following file contains the local settings for the application.
from pathlib import Path

# The base directory of the project (default is 'src')
BASE_DIR = Path(__file__).resolve().parent.parent

# Whenever the site should be on debug or not (display errors, etc.)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret! (for development can be anything)
SECRET_KEY = 'random-insecure-key-asgshgjshgfvbhgbjshgfhsdgjfbgrhjgfbjhg2356uhtgr&$%%^&*()_+'

# When DEBUG is False, in case of a code error, the ADMINS will be notified on their email address.
ADMINS = []

# Static files (css, javascript, images)
# The path from which the server will serve static files (used in production)
# If you don't know what this is, put the path to a folder called 'static' in the root of the project (D:\Programming\Python\Project-6.1\static - for example)
STATIC_ROOT = "/static"

# Media files
MEDIA_ROOT = BASE_DIR / 'media'

# A list of directories where Django looks for static files
STATICFILES_DIRS = [BASE_DIR / 'static']

# Credentials for the SQL database (MySQL or MariaDB)
DB_PASS = ""
DB_USER = "root"
DB_HOST = "db"
DB_NAME = "sports_accounting"
DB_PORT = 3306

# Credentials for the backup SQL database
DB_BACKUP_PASS = "root"
DB_BACKUP_USER = "Passw0rd!"

# Credentials for the NoSQL DB
MONGO_DB_DATABASE = "SportsAccounting"
MONGO_DB_CLUSTER = "Transactions"

MONGO_DB_PASSWORD = "Passw0rd!"
MONGO_DB_URI = "mongodb+srv://<username>:<password>@<cluster>/<database>?retryWrites=true&w=majority"
