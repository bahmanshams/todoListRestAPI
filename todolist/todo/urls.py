from django.urls import path
from . import views

urlpatterns = [
    path('all_todo/',views.all_todo, name='all_todo'),
    path('all_cat/',views.all_cat, name='all_cat'),
    # path('insert_todo/',views.insert_todo, name='insert_todo'),
    # path('update_todo/',views.update_todo, name='update_todo'),
    # path('delete_todo/',views.delete_todo, name='delete_todo'),
]