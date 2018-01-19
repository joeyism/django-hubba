from hubba_products import data
from django.core.management.base import BaseCommand, CommandError
from hubba_products import recommendations

def gen_recommendations():
    recommendations.generate()

class Command(BaseCommand):

    def handle(self, *args, **options):
        gen_recommendations()

if __name__ == "__main__" or __name__ == "django.core.management.commands.shell":
    gen_recommendations()
