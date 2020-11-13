from catalog import database as db

database = db.Database()
database.fetch_categories()
database.fetch_products()
database.fill_database()