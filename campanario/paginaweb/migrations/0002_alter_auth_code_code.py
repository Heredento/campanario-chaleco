# Generated by Django 4.1 on 2022-08-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginaweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth_code',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]