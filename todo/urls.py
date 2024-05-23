from django.urls import path
from . import views
urlpatterns = [
    path('', views.todos, name='index'),
    path('<int:todo_id>', views.todo_detail),

]