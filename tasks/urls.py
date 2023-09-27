from django.urls import path
from .import views
urlpatterns = [
    path('',views.login,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('tasks',views.tasks,name='tasks'),
    path('c_task',views.create_task,name = 'c_task'),
    path('mark_finished/<int:task_id>',views.mark_finished,name='mark_finished'),
    path('delete_task/<int:task_id>',views.delete_task,name='delete_task'),
]

