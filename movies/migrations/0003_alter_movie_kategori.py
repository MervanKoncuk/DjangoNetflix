# Generated by Django 3.2.12 on 2022-06-26 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220626_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.category'),
        ),
    ]