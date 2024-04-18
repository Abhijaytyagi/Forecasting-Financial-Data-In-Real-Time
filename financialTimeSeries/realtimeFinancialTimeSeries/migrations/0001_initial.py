# Generated by Django 4.2.7 on 2023-11-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Quarter', models.CharField(max_length=2)),
                ('Year', models.CharField(max_length=4)),
                ('feature', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='TargetVariable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Target', models.CharField(max_length=100)),
            ],
        ),
    ]