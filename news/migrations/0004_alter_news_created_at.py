# Generated by Django 4.2.3 on 2024-01-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(),
        ),
    ]
