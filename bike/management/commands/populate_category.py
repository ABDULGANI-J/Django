from bike.models import Category
from django.core.management import BaseCommand



class Command(BaseCommand):
    help = "This Command inserts category data"

    def handle(self, *args, **options):
            Category.objects.all().delete()

            category = ['Sports','Milage','Performanace','Budget']
           
            for category_name in category:
                Category.objects.create(name=category_name)

            self.stdout.write(self.style.SUCCESS("commpleted inserting data!"))