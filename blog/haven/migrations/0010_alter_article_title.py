# Generated by Django 5.1.6 on 2025-02-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haven', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
