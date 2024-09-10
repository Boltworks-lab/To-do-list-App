from django.urls import path
from .views import HomePageView, task_list, task_detail, task_add, task_edit, task_delete, task_completed

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('task/', task_list, name = 'task_list'),
    path('task/new/', task_add, name = 'task_add'),
    path('detail/<int:pk>/', task_detail, name = 'task_details'),
    path('edit/<int:pk>/', task_edit, name = 'task_edit'),
    path('delete/<int:pk>/', task_delete, name = 'task_delete'),
    path('complete/<int:pk>/', task_completed, name = 'task_complete')
]