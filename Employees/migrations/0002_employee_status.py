# Generated by Django 3.2rc1 on 2021-04-21 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Status',
            field=models.CharField(default='Assigned', max_length=20),
        ),
    ]