from pymongo import MongoClient
from sports_accounting import settings

# MongoDB connection
client = MongoClient(settings.MONGO_DB_URI)
# Define the database
db = client["SportsAccounting"]
# Define the collections (same as tables in SQL)
transactions_collection = db["Transactions"]
