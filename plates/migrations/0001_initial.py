# Generated by Django 2.1.7 on 2019-03-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plateNumber', models.IntegerField()),
                ('street', models.CharField(max_length=255)),
                ('zipCode', models.IntegerField()),
                ('city', models.TextField(max_length=100)),
            ],
        ),
    ]
