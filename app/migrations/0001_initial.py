# Generated by Django 5.0.3 on 2024-03-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=4)),
                ('date', models.DateField()),
                ('revenue', models.CharField(max_length=50)),
                ('gp', models.CharField(max_length=50)),
                ('fcf', models.CharField(max_length=50)),
                ('capex', models.CharField(max_length=50)),
            ],
        ),
    ]
