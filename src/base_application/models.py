from src.base_application import db


# Models used in the NoSQL database - similar to an ORM
class Transaction(db.Document):
	def to_json(self):
		pass
