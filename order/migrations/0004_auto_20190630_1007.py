# Generated by Django 2.2.1 on 2019-06-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_bugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
