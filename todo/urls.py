from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',views.TodoViewSetAPIView)

urlpatterns = [
    path('', views.ManageTodoView.as_view(), name='index'),
    path('<int:todo_id>', views.TodoDetailView.as_view(), name='detail'),
    path('mixins/', views.TodoListMixinsView.as_view()),
    path('mixins/<pk>', views.TodoDetailMixinsView.as_view()),
    path('generics/', views.TodoGenericAPIView.as_view()),
    path('generics/<pk>', views.TodoGenericDetailAPIView.as_view()),
    path('viewsets/', include(router.urls)),

]
