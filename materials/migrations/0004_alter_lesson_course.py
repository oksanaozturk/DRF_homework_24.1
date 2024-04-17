# Generated by Django 5.0.4 on 2024-04-16 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_remove_course_lessons_lesson_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]