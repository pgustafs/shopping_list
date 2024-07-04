import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from shopping_list.models import Household, Item, Category, HouseholdItem

# Define categories with descriptions
categories_data = [
    {"name": "Fruits", "description": "Apples, bananas,  grapes, oranges, strawberries, avocados, peaches, etc."},
    {"name": "Vegetables", "description": "Potatoes, onions, carrots, salad greens, broccoli, peppers, tomatoes, cucumbers, etc."},
    {"name": "Canned Goods", "description": "Soup, tuna, fruit, beans, vegetables, pasta sauce, etc."},
    {"name": "Dairy", "description": "Butter, cheese, eggs, milk, yogurt, etc."},
    {"name": "Meat", "description": "Chicken, beef, pork, sausage, bacon etc."},
    {"name": "Fish & Seafood", "description": "Shrimp, crab, cod, tuna, salmon, etc."},
    {"name": "Deli", "description": "Cheese, salami, ham, turkey, etc."},
    {"name": "Condiments & Spices", "description": "Black pepper, oregano, cinnamon, sugar, olive oil, ketchup, mayonnaise, etc."},
    {"name": "Snacks", "description": "Chips, pretzels, popcorn, crackers, nuts, etc."},
    {"name": "Bread & Bakery", "description": "Bread, tortillas, pies, muffins, bagels, cookies, etc."},
    {"name": "Beverages", "description": "Coffee, teabags, milk, juice, soda, beer, wine, etc."},
    {"name": "Pasta, Rice & Cereal", "description": "Oats, granola, brown rice, white rice, macaroni, noodles, etc."},
    {"name": "Baking", "description": "Flour, powdered sugar, baking powder, cocoa etc."},
    {"name": "Frozen Foods", "description": "Pizza, fish, potatoes, ready meals, ice cream, etc."},
    {"name": "Personal Care", "description": "Shampoo, conditioner, deodorant, toothpaste, dental floss, etc."},
    {"name": "Health Care", "description": "Saline, band-aid, cleaning alcohol, pain killers, antacids, etc."},
    {"name": "Household & Cleaning Supplies", "description": "Laundry detergent, dish soap, dishwashing liquid, paper towels, tissues, trash bags, aluminum foil, zip bags, etc."},
    {"name": "Baby Items", "description": "Baby food, diapers, wet wipes, lotion, etc."},
    {"name": "Pet Care", "description": "Pet food, kitty litter, chew toys, pet treats, pet shampoo, etc."},
]

# Create categories
categories = {}
for category_data in categories_data:
    category, created = Category.objects.get_or_create(
        name=category_data["name"], 
        defaults={"description": category_data["description"]}
    )
    categories[category_data["name"]] = category

# Create households
household_names = ["Household 1", "Household 2", "Household 3"]
households = []
for name in household_names:
    household, created = Household.objects.get_or_create(name=name, slug=name.lower().replace(" ", "-"))
    households.append(household)

# Define items with specific categories
items_data = [
    {"name": "Apple", "category": "Fruits"},
    {"name": "Banana", "category": "Fruits"},
    {"name": "Carrot", "category": "Vegetables"},
    {"name": "Milk", "category": "Dairy"},
    {"name": "Chicken", "category": "Meat"},
    {"name": "Salmon", "category": "Fish & Seafood"},
    {"name": "Ham", "category": "Deli"},
    {"name": "Ketchup", "category": "Condiments & Spices"},
    {"name": "Chips", "category": "Snacks"},
    {"name": "Bread", "category": "Bread & Bakery"},
    {"name": "Juice", "category": "Beverages"},
    {"name": "Pasta", "category": "Pasta, Rice & Cereal"},
    {"name": "Flour", "category": "Baking"},
    {"name": "Ice Cream", "category": "Frozen Foods"},
    {"name": "Shampoo", "category": "Personal Care"},
    {"name": "Vitamins", "category": "Health Care"},
    {"name": "Detergent", "category": "Household & Cleaning Supplies"},
    {"name": "Diapers", "category": "Baby Items"},
    {"name": "Dog Food", "category": "Pet Care"},
]

# Create items and household items with random counts
for item_data in items_data:
    category = categories[item_data["category"]]
    item, created = Item.objects.get_or_create(name=item_data["name"], category=category)
    
    for household in households:
        quantity = random.randint(1, 10)
        add_count = random.randint(0, 20)
        HouseholdItem.objects.create(household=household, item=item, quantity=quantity, add_count=add_count)

print("Test data created successfully.")