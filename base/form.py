from django import forms
from django.forms import ModelForm

from base.models import EmployeDetail


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeDetail
        fields = '__all__'

        exclude=['joining']



