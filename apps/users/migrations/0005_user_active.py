# Generated by Django 4.1.6 on 2023-02-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_company_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
