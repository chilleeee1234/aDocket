from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from task_management_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.taskView, 'task')

urlpatterns = [
    path('', admin.site.urls),
    path('', include(router.urls)),
]
