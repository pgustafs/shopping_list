from django.db import models

# Create your models here.
class Household(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class HouseholdItem(models.Model):
    household = models.ForeignKey(Household, related_name='household_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='household_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    add_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} in {self.household.name}"