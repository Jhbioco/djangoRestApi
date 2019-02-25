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
