# Generated by Django 2.2.5 on 2021-07-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210701_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='portal',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]