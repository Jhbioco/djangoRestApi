from rest_framework import serializers
from .models import Employee
from .models import Department
from .models import Category


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('url', 'id', 'name', 'department', 'category')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'dep_acronym', 'dep_name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'cat_name', 'cat_salary')




