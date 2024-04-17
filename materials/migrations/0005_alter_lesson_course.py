# Generated by Django 5.0.4 on 2024-04-17 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0004_alter_lesson_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
