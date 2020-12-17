from django.core.management.base import BaseCommand

from catalog import database as db
class Command(BaseCommand):
    def handle(self, *args, **options):
        database = db.Database()
        database.fetch_categories()
        database.fetch_products()
        database.fill_database()