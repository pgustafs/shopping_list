from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('add_idem/', views.add_item, name='add_item'),
    path('households/', views.household_list, name='household_list'),
    path('household/<slug:slug>/', views.household_detail, name='household_detail'),
    path('household/<slug:slug>/add-item/', views.add_item, name='add_item'),
    path('household/<slug:slug>/clear-items/', views.clear_items, name='clear_items'),
    path('household/<slug:slug>/delete-selected-items/', views.delete_selected_items, name='delete_selected_items'),
    path('item/<int:pk>/from-household/<slug:slug>/', views.item_detail_from_household, name='item_detail_from_household'),
    path('all-items/', views.all_items, name='all_items'),
    path('item/<int:pk>/from-all/', views.item_detail_from_all, name='item_detail_from_all'),
    path('add-item/', views.add_item_from_all, name='add_item_from_all'),
    path('categories/', views.category_list, name='category_list'),
    path('add-category/', views.add_category, name='add_category'),
]