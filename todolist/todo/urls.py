from django.urls import path
from . import views

urlpatterns = [
    path('all_todo/',views.all_todo, name='all_todo'),
    path('all_subset/',views.all_subset, name='all_subset'),
    path('all_subset_filtered_todo/',views.all_subset_filtered_todo, name='all_subset_filtered_todo'),
    path('all_todo_filtered_today/',views.all_todo_filtered_today, name='all_todo_filtered_today'),
    path('all_todo_filtered_yesterday/',views.all_todo_filtered_yesterday, name='all_todo_filtered_yesterday'),
    path('all_todo_filtered_tomorrow/',views.all_todo_filtered_tomorrow, name='all_todo_filtered_tomorrow'),
    path('all_todo_filtered_current_week/',views.all_todo_filtered_current_week, name='all_todo_filtered_current_week'),
    path('all_todo_filtered_next_week/',views.all_todo_filtered_next_week, name='all_todo_filtered_next_week'),
    path('all_todo_filtered_last_week/',views.all_todo_filtered_last_week, name='all_todo_filtered_last_week'),
    path('all_todo_filtered_cat/',views.all_todo_filtered_cat, name='all_todo_filtered_cat'),
    path('all_todo_filtered_date/',views.all_todo_filtered_date, name='all_todo_filtered_date'),
    path('all_todo_filtered_date_range/',views.all_todo_filtered_date_range, name='all_todo_filtered_date_range'),
    path('all_todo_filtered_status/',views.all_todo_filtered_status, name='all_todo_filtered_status'),
    path('all_cat/',views.all_cat, name='all_cat'),
    path('insert_todo/',views.insert_todo, name='insert_todo'),
    path('insert_subset/',views.insert_subset, name='insert_subset'),
    path('insert_cat/',views.insert_cat, name='insert_cat'),
    path('update_cat/',views.update_cat, name='update_cat'),
    path('update_todo/',views.update_todo, name='update_todo'),
    path('update_subset/',views.update_subset, name='update_subset'),
    path('delete_cat/',views.delete_cat, name='delete_cat'),
    path('delete_todo/',views.delete_todo, name='delete_todo'),
    path('delete_subset/',views.delete_subset, name='delete_subset'),
]