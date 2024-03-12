# Generated by Django 5.0.3 on 2024-03-12 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='generic.author'),
        ),
    ]