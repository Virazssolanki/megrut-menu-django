# Generated by Django 2.2.1 on 2019-09-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190909_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='menuphoto'),
        ),
    ]
