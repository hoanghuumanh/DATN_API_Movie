# Generated by Django 3.1.2 on 2020-10-07 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie', models.CharField(max_length=70)),
                ('Year', models.DateField()),
                ('Content', models.TextField()),
                ('Image', models.FileField(upload_to='img/')),
                ('Rate', models.IntegerField()),
                ('Categori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movie.category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phonenum', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('cmmd', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_u', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movie.movie')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movie.profile')),
            ],
        ),
    ]
