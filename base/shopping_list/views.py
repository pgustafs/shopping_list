from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Household, Category, Item
from .forms import ItemForm, CategoryForm

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'shopping_list/index.html', {'categories': categories})

def household_list(request):
    households = Household.objects.all()
    return render(request, 'shopping_list/households.html', {'households': households})

def household_detail(request, slug):
    household = get_object_or_404(Household, slug=slug)
    items = household.items.select_related('category').all()
    return render(request, 'shopping_list/household_detail.html', {'household': household, 'items': items})

def add_item(request, slug):
    household = get_object_or_404(Household, slug=slug)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.household = household
            item.save()
            return redirect('household_detail', slug=slug)
    else:
        form = ItemForm()
    return render(request, 'shopping_list/add_item.html', {'form': form, 'household': household})

def clear_items(request, slug):
    household = get_object_or_404(Household, slug=slug)
    household.items.all().delete()
    return redirect('household_detail', slug=slug)

def delete_selected_items(request, slug):
    household = get_object_or_404(Household, slug=slug)
    if request.method == 'POST':
        items_to_delete = request.POST.getlist('items_to_delete')
        Item.objects.filter(id__in=items_to_delete, household=household).delete()
    return redirect('household_detail', slug=slug)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shopping_list/item_detail.html', {'item': item})

# Items views
def all_items(request):
    items = Item.objects.select_related('category').all()
    return render(request, 'shopping_list/all_items.html', {'items': items})

# Category views
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'shopping_list/add_category.html', {'form': form})