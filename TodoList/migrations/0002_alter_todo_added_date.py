# Generated by Django 3.2.9 on 2021-12-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(),
        ),
    ]
