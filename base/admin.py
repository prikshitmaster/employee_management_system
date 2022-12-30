from django.contrib import admin

from base.models import EmployeDetail, Department, Role

# Register your models here.

admin.site.register(EmployeDetail)
admin.site.register(Department)
admin.site.register(Role)