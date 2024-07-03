import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from shopping_list.models import Household, Category, Item, HouseholdItem

def create_test_data():
    # Create households
    household1 = Household.objects.create(name="Household 1", slug="household-1")
    household2 = Household.objects.create(name="Household 2", slug="household-2")

    # Create categories
    category_names = [
        "Fruits", "Vegetables", "Canned Goods", "Dairy", "Meat", "Fish & Seafood",
        "Deli", "Condiments & Spices", "Snacks", "Bread & Bakery", "Beverages",
        "Pasta, Rice & Cereal", "Baking", "Frozen Foods", "Personal Care",
        "Health Care", "Household & Cleaning Supplies", "Baby Items", "Pet Care"
    ]
    
    categories = {}
    for name in category_names:
        categories[name] = Category.objects.create(name=name)
    
    # Create items
    items = {
        "Apple": categories["Fruits"],
        "Banana": categories["Fruits"],
        "Carrot": categories["Vegetables"],
        "Tomato": categories["Vegetables"],
        "Canned Beans": categories["Canned Goods"],
        "Canned Corn": categories["Canned Goods"],
        "Milk": categories["Dairy"],
        "Cheese": categories["Dairy"],
        "Chicken Breast": categories["Meat"],
        "Ground Beef": categories["Meat"],
        "Salmon": categories["Fish & Seafood"],
        "Shrimp": categories["Fish & Seafood"],
        "Ham": categories["Deli"],
        "Turkey": categories["Deli"],
        "Ketchup": categories["Condiments & Spices"],
        "Salt": categories["Condiments & Spices"],
        "Chips": categories["Snacks"],
        "Cookies": categories["Snacks"],
        "Bread": categories["Bread & Bakery"],
        "Bagel": categories["Bread & Bakery"],
        "Juice": categories["Beverages"],
        "Soda": categories["Beverages"],
        "Pasta": categories["Pasta, Rice & Cereal"],
        "Rice": categories["Pasta, Rice & Cereal"],
        "Flour": categories["Baking"],
        "Sugar": categories["Baking"],
        "Frozen Pizza": categories["Frozen Foods"],
        "Ice Cream": categories["Frozen Foods"],
        "Shampoo": categories["Personal Care"],
        "Toothpaste": categories["Personal Care"],
        "Aspirin": categories["Health Care"],
        "Band-Aids": categories["Health Care"],
        "Detergent": categories["Household & Cleaning Supplies"],
        "Paper Towels": categories["Household & Cleaning Supplies"],
        "Diapers": categories["Baby Items"],
        "Baby Food": categories["Baby Items"],
        "Dog Food": categories["Pet Care"],
        "Cat Litter": categories["Pet Care"]
    }

    item_objects = {}
    for name, category in items.items():
        item_objects[name] = Item.objects.create(name=name, category=category)

    # Create household items
    HouseholdItem.objects.create(household=household1, item=item_objects["Apple"], quantity=5)
    HouseholdItem.objects.create(household=household1, item=item_objects["Milk"], quantity=2)
    HouseholdItem.objects.create(household=household1, item=item_objects["Chicken Breast"], quantity=3)
    HouseholdItem.objects.create(household=household2, item=item_objects["Rice"], quantity=1)
    HouseholdItem.objects.create(household=household2, item=item_objects["Cheese"], quantity=1)
    HouseholdItem.objects.create(household=household2, item=item_objects["Ice Cream"], quantity=4)

    print("Test data created successfully.")

if __name__ == "__main__":
    create_test_data()