# Generated by Django 4.1.4 on 2022-12-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_employedetail_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employedetail',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
