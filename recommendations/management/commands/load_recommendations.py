from django.core.management.base import BaseCommand, CommandError
from hubba_products import data
from hubba_products import recommendations
from recommendations.models import Buyer, Recommendation, Product

def load_recommendations():
    recomm = recommendations.get()
    for user_id, context_product_list in recomm.items():
        buyer = Buyer.objects.get(owner = user_id)
        for context_product in context_product_list:
            product = Product.objects.get(name=context_product)
            recomm_model = Recommendation(
                    buyer = buyer,
                    product = product,
                    user_id = user_id,
                    context_product = context_product
                    )
            recomm_model.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_recommendations()

if __name__ == "__main__" or __name__ == "django.core.management.commands.shell":
    load_recommendations()
