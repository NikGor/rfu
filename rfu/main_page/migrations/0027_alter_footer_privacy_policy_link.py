# Generated by Django 4.1.7 on 2023-12-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0026_remove_footer_legal_links_footer_email_part1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footer",
            name="privacy_policy_link",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
