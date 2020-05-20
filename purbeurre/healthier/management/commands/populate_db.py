import requests
import json

from django.core.management.base import BaseCommand, CommandError

from ...models import Store, Brand, Category, Food_item

class Command(BaseCommand):
    help = "IMPORT DATA FROM OpenFoodFacts given a category list or all categories"

    def add_arguments(self, parser):
        parser.add_argument("categories", nargs="+", type=str)
    
    def handle(self, *args, **options):
        if "all" in options:
            self.populate_with()
        else:
            for categorie in options["categories"]:
                self.populate_with(categorie)
    
    def populate_with(self, categorie=all):
        if categorie == "all":
            # download the list of all catégories from OFF
            request = requests.get("https://fr.openfoodfacts.org/categorie/{}.json".format(categorie))
            if request.status_code == 200:
                # download the food items from OFF that have nutriscore and novagrade
                categories = {tag["name"] for tag in json.load(request.json())}
                self.stdout.write("categories downloaded")
                for categorie in categories:
                    food_items = self.get_fooditems(categorie)
                    self.stdout.write(food_items)
                
                # populate DB
            else:
                raise CommandError('unable to download categories (other than 200...)')
                
        else:
            # download the food items of the categorie from OFF that have nutriscore and novagrade
            food_items = self.get_fooditems(categorie)
            self.stdout.write(str(food_items), ending="")
            # populate DB
            pass

    def get_fooditems(self, categorie, number=500, fields=["url"]):
        #returns all fooditems with nova and nutri in a list max number=1000
        self.stdout.write("beginning downloading items for category {}".format(categorie))
        request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",
                                        params={"action":"process",
                                                "tagtype_0":"categories",
                                                "tag_contains_0":"contains",
                                                "tag_0":categorie,
                                                "json":"true",
                                                "fields": ",".join(fields),
                                                "page_size":str(number)+"#"+str(number),
                                                }
                                )
        if request.status_code == 200:
            return request.json()
        else:
            raise CommandError('unable to download fooditems for category {}'.format(categorie))







