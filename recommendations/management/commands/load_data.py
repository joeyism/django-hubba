from recommendations.models import Product, Buyer, Action
from hubba_products import data
from django.core.management.base import BaseCommand, CommandError


def load_data():
    prods = data.get_prods()
    for i, row in prods.iterrows():
        product = Product(
            name = row["name"],
            picture_url = row["picture"],
            description = row["description"],
            product_name = row["product_name"]
        )
        product.save()

    buyers = data.get_buyers()
    for i, row in buyers.iterrows():
        buyer = Buyer(
            owner = row["owner"],
            name = row["name"],
            description = row["description"]
        )
        buyer.save()

    actions = data.get_actions()
    for i, row in actions.iterrows():
        buyer = Buyer.objects.get(owner=row["user_id"])
        product = Product.objects.get(name=row["context_product"])
        action = Action(
            buyer = buyer,
            product = product,
            user_id = row["user_id"],
            context_product = row["context_product"],
            no_of_actions = row["positive_action_count"]
        )
        action.save()


    return


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_data()

if __name__ == "__main__" or __name__ == "django.core.management.commands.shell":
    load_data()
