# Generated by Django 4.1.4 on 2022-12-29 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_department_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='roles',
            field=models.CharField(max_length=100),
        ),
    ]
