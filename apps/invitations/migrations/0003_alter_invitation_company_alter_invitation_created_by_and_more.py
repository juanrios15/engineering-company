# Generated by Django 4.1.6 on 2023-02-10 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("companies", "0004_alter_company_logo"),
        ("invitations", "0002_alter_invitation_created_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invitation",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="companies.company",
            ),
        ),
        migrations.AlterField(
            model_name="invitation",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="invitation",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]