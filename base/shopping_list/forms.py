from django import forms
from .models import Item, Category, HouseholdItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class HouseholdItemForm(forms.ModelForm):
    class Meta:
        model = HouseholdItem
        fields = ['item', 'quantity']