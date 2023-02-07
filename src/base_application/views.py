from src.base_application import app
from src.base_application import db


# Views (API)

@app.route("/")
def index():
	db.insert_one({"name": "Smth"})
	return "Hello World!"


@app.route("/api/getTransactionsAmount", methods=["GET"])
def get_transactions_amount():
	return db.count_documents({})


@app.route("/api/uploadMT940File", methods=["POST"])
def send_file():
	return "Hello World!"
