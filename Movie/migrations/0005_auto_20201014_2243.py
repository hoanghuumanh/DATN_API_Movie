# Generated by Django 3.1.2 on 2020-10-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0004_auto_20201014_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]
