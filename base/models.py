import datetime

from django.db import models


# Create your models here.

class Role(models.Model):
    roles = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.roles


class Department(models.Model):
    dept = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.dept


class EmployeDetail(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    salary = models.IntegerField(max_length=7, null=True)
    bonus = models.IntegerField(max_length=7, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    joining = models.DateField(auto_created=True , null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fullname
