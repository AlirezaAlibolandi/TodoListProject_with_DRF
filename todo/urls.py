from django.urls import path
from . import views
urlpatterns = [
    path('', views.ManageTodoView.as_view(), name='index'),
    path('<int:todo_id>', views.TodoDetailView.as_view(), name='detail'),

]