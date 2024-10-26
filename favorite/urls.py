from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path('', views.show_main_favorite, name='favorite_list_view'),
    path('add-to-favorite/<int:restaurant_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('list-all-restaurants/', views.list_all_restaurants, name='list_all_restaurants'),
    path('add-to-favorite-ajax/', views.add_to_favorite_ajax, name='add_to_favorite_ajax'),
    path('delete-favorite/', views.delete_favorite, name='delete_favorite'),
    path('edit/', views.edit_favorite_notes, name='edit_favorite_notes'),
]
