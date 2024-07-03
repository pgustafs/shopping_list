import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from shopping_list.models import Household, Category, Item

def create_test_data():
    # Create households
    household1 = Household.objects.create(name="Household 1", slug="household-1")
    household2 = Household.objects.create(name="Household 2", slug="household-2")

    # Create categories
    category1 = Category.objects.create(name="Dairy")
    category2 = Category.objects.create(name="Bakery")
    category3 = Category.objects.create(name="Produce")

    # Create items for the households
    Item.objects.create(household=household1, category=category1, name="Milk", quantity=2)
    Item.objects.create(household=household1, category=category2, name="Bread", quantity=1)
    Item.objects.create(household=household2, category=category3, name="Eggs", quantity=12)
    Item.objects.create(household=household2, category=category1, name="Butter", quantity=1)

    print("Test data created successfully.")

if __name__ == "__main__":
    create_test_data()