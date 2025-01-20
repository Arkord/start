# Generated by Django 5.1.5 on 2025-01-19 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0005_author_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='app_one.author'),
        ),
    ]
