# Generated by Django 2.2.1 on 2019-09-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190908_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='menuphoto'),
        ),
    ]