# Generated by Django 5.0.4 on 2024-04-13 20:53

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользоаптель",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите изображение",
                null=True,
                upload_to="users_avatar",
                verbose_name="Аватар пользователя",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="counter",
            field=models.CharField(
                blank=True,
                help_text="Введите страну проживания",
                max_length=100,
                null=True,
                verbose_name="Страна",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="Укажите Ваш номер телефона",
                max_length=128,
                null=True,
                region=None,
                verbose_name="Номер телефона",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Введите email",
                max_length=150,
                unique=True,
                verbose_name="email",
            ),
        ),
    ]
