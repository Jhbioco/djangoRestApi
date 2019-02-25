# DRF
A basic employee-api with django rest framework.
# First Steps
Before starting the web api based on django rest framework its necessary install all dependencies as we always do when start developing django projects. Good practices says that we have to setup a new python environment for each time we start a django project.
```
virtualenv virtual
```
virtual is the name of the pythons virtual environment. After that we have to activate this virtual environment by doing:
```
source virtual/bin/activate
```
**Django and Django Rest Framework installations**
```
pip install django
```
```
pip install djangorestframework
```
**Starting the project and the app**
```
django-admin startproject myrestproject
```
```
django-admi startapp rest
```
Now the django project (myrestproject) and our application (rest) are created. Next we will create the superuser and then do the migration for the first time.
```
cd myproject
```
```
python manage.py createsuperuser
```
```
Username (leave blank to use 'computer-user'): 
Email address: 
Password:
```
```
python manage.py migrate
```
# The API
**Setting.py**

We just made basic changes in settings.py file: 

1) Add in installed_apps the name of our application (rest) and the rest_framework; 
```

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest',
    'rest_framework',
]
```
2) Insert default permission classes of the rest_framework in order to access only authenticated users.
```
REST_FRAMEWORK= {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',)
}
```
#
***myrestproject/urls.py***
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('rest.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
```
#
**rest/models.py**
```
from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_salary = models.FloatField(blank=True)

    def __str__(self):
        return self.cat_name


class Department(models.Model):
    dep_acronym = models.CharField(max_length=10)
    dep_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_acronym + ' - ' + self.dep_name


class Employee(models.Model):
    name = models.CharField(max_length=40)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```
#
**rest/serializers.py**
```
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
```
#
**rest/views.py**
```
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
```
#
**rest/urls.py**

Dont forget to create _urls.py_ inside rest folder.
```
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
```

