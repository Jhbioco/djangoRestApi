from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Employee
from .models import Department
from .models import Category
from .serializers import EmployeeSerializer
from .serializers import DepartmentSerializer
from .serializers import CategorySerializer


# Create your views here.
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer