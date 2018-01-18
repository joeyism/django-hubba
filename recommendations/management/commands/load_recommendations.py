from django.core.management.base import BaseCommand, CommandError
from hubba_products import data

def load_recommendations():

    return


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_recommendations()

if __name__ == "__main__" or __name__ == "django.core.management.commands.shell":
    load_recommendations()
