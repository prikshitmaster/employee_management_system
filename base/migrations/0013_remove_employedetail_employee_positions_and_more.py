# Generated by Django 4.1.4 on 2022-12-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_department_dept_alter_department_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employedetail',
            name='employee_positions',
        ),
        migrations.AlterField(
            model_name='department',
            name='dept',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='roles',
            field=models.CharField(max_length=100, null=True),
        ),
    ]