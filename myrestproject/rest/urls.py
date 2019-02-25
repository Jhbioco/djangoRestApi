from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', views.EmployeeView),
router.register('department', views.DepartmentView),
router.register('category', views.CategoryView)
urlpatterns = [
    path('', include(router.urls))
]
