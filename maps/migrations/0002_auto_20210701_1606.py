# Generated by Django 2.2.5 on 2021-07-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position1', models.CharField(max_length=15)),
                ('position2', models.CharField(max_length=15)),
                ('position3', models.CharField(max_length=15)),
                ('position4', models.CharField(max_length=15)),
                ('position5', models.CharField(max_length=15)),
                ('position6', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
