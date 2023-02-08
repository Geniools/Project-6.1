# from flask_mongoengine import MongoEngine
from flask import Flask
from pymongo import MongoClient

from local_settings import MONGO_DB_URI

# Flask application
app = Flask(__name__)
# app.config["MONGODB_HOST"] = MONGO_DB_URI

# MongoDB engine (used for models like an ORM)
# db_engine = MongoEngine(app)

# MongoDB connection
client = MongoClient(MONGO_DB_URI)
# Define the database
db = client["SportsAccounting"]
# Define the collections (same as tables in SQL)
transactions_collection = db["Transactions"]

# Import views (must be imported after app, so that the app is aware of the API/views)
from src.base_application import views
