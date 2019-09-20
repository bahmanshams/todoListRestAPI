from django.urls import path
from . import views

urlpatterns = [
    path('all_todo/',views.all_todo, name='all_todo'),
    path('all_cat/',views.all_cat, name='all_cat'),
    path('insert_todo/',views.insert_todo, name='insert_todo'),
    path('insert_cat/',views.insert_cat, name='insert_cat'),
    # path('update_todo/',views.update_todo, name='update_todo'),
    path('delete_cat/',views.delete_cat, name='delete_cat'),
    path('delete_todo/',views.delete_todo, name='delete_todo'),
]