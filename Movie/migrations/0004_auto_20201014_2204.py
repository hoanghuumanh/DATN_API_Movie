# Generated by Django 3.1.2 on 2020-10-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0003_auto_20201012_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Image',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]