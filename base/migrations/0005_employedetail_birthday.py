# Generated by Django 4.1.4 on 2022-12-29 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_employedetail_employee_positions'),
    ]

    operations = [
        migrations.AddField(
            model_name='employedetail',
            name='birthday',
            field=models.DateField(null=True, verbose_name=datetime.date),
        ),
    ]