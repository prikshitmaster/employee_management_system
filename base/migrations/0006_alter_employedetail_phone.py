# Generated by Django 4.1.4 on 2022-12-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_employedetail_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedetail',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
