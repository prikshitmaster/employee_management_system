# Generated by Django 4.1.4 on 2022-12-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_employedetail_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='employedetail',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
