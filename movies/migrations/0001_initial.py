# Generated by Django 3.2.12 on 2022-06-26 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='filmler/', verbose_name='Film Resmi')),
                ('name', models.CharField(max_length=200)),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.category')),
            ],
        ),
    ]
