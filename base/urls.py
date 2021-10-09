from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create-task',views.createTask,name='create-task'),
    path('task/<int:id>',views.viewTask,name='view-task'),
    path('<int:id>/delete',views.deleteTask,name='delete-task'),
    path('<int:id>/complete',views.completeTask,name='complete-task'),
    path('<int:id>/incomplete',views.incompleteTask,name='incomplete-task'),
]
