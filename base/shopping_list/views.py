from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Household, Category, Item, HouseholdItem
from .forms import ItemForm, CategoryForm, HouseholdItemForm, HouseholdForm

# Create your views here.

def index(request):
    return render(request, 'shopping_list/index.html')

def add_household(request):
    if request.method == 'POST':
        form = HouseholdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('household_list')
    else:
        form = HouseholdForm()
    return render(request, 'shopping_list/add_household.html', {'form': form})

def household_list(request):
    households = Household.objects.all()
    return render(request, 'shopping_list/households.html', {'households': households})

def household_detail(request, slug):
    household = get_object_or_404(Household, slug=slug)
    category_id = request.GET.get('category')
    if category_id:
        household_items = household.household_items.filter(item__category_id=category_id).select_related('item', 'item__category').all()
    else:
        household_items = household.household_items.select_related('item', 'item__category').all()
    categories = Category.objects.all()
    return render(request, 'shopping_list/household_detail.html', {'household': household, 'household_items': household_items, 'categories': categories, 'selected_category': category_id})

def add_item(request, slug):
    household = get_object_or_404(Household, slug=slug)
    if request.method == 'POST':
        form = HouseholdItemForm(request.POST)
        if form.is_valid():
            household_item = form.save(commit=False)
            household_item.household = household
            household_item.add_count += 1
            household_item.save()
            return redirect('household_detail', slug=slug)
    else:
        form = HouseholdItemForm()
    return render(request, 'shopping_list/add_item.html', {'form': form, 'household': household})

def clear_items(request, slug):
    household = get_object_or_404(Household, slug=slug)
    household.household_items.all().delete()
    return redirect('household_detail', slug=slug)

def delete_selected_items(request, slug):
    household = get_object_or_404(Household, slug=slug)
    if request.method == 'POST':
        items_to_delete = request.POST.getlist('items_to_delete')
        HouseholdItem.objects.filter(id__in=items_to_delete, household=household).delete()
    return redirect('household_detail', slug=slug)

def item_detail_from_household(request, pk, slug):
    item = get_object_or_404(Item, pk=pk)
    household = get_object_or_404(Household, slug=slug)
    return render(request, 'shopping_list/item_detail_from_household.html', {'item': item, 'household': household})

def items_sorted_by_count(request, slug):
    household = get_object_or_404(Household, slug=slug)
    household_items = household.household_items.select_related('item', 'item__category').order_by('-add_count')

    # Prepare data for the chart
    categories = []
    items_data = {}
    for household_item in household_items:
        category_name = household_item.item.category.name
        item_name = household_item.item.name
        add_count = household_item.add_count

        if category_name not in categories:
            categories.append(category_name)
        
        if item_name not in items_data:
            items_data[item_name] = [0] * len(categories)
        
        items_data[item_name][categories.index(category_name)] = add_count

    chart_data = {
        'categories': categories,
        'items': list(items_data.keys()),
        'data': list(items_data.values())
    }

    return render(request, 'shopping_list/items_sorted_by_count.html', {
        'household': household,
        'chart_data': chart_data
    })

# Item views
def all_items(request):
    category_id = request.GET.get('category')
    if category_id:
        items = Item.objects.filter(category_id=category_id).select_related('category').all()
    else:
        items = Item.objects.select_related('category').all()
    categories = Category.objects.all()
    return render(request, 'shopping_list/all_items.html', {'items': items, 'categories': categories, 'selected_category': category_id})

def item_detail_from_all(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shopping_list/item_detail_from_all.html', {'item': item})

def add_item_from_all(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_items')
    else:
        form = ItemForm()
    return render(request, 'shopping_list/add_item_from_all.html', {'form': form})

# Category views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shopping_list/category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'shopping_list/add_category.html', {'form': form})