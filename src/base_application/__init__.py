from flask import Flask
from flask_mongoengine import MongoEngine

from local_settings import MONGO_DB_URI

# Flask application
app = Flask(__name__)
app.config["MONGODB_HOST"] = MONGO_DB_URI

# MongoDB connection
db = MongoEngine(app)

# Import views (must be imported after app, so that the app is aware of the API/views)
from src.base_application import views
