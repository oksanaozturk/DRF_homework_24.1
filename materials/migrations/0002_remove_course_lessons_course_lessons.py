# Generated by Django 5.0.4 on 2024-04-16 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="lessons",
        ),
        migrations.AddField(
            model_name="course",
            name="lessons",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.lesson",
                verbose_name="Уроки",
            ),
        ),
    ]
