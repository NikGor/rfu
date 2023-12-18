# Generated by Django 4.1.7 on 2023-12-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0023_ourwork_text_de_ourwork_text_en_ourwork_text_pl_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HelpUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("title_en", models.CharField(blank=True, max_length=100, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=100, null=True)),
                ("title_ua", models.CharField(blank=True, max_length=100, null=True)),
                ("title_pl", models.CharField(blank=True, max_length=100, null=True)),
                ("title_de", models.CharField(blank=True, max_length=100, null=True)),
                ("text", models.TextField(blank=True, max_length=500, null=True)),
                ("text_en", models.TextField(blank=True, max_length=500, null=True)),
                ("text_ru", models.TextField(blank=True, max_length=500, null=True)),
                ("text_ua", models.TextField(blank=True, max_length=500, null=True)),
                ("text_pl", models.TextField(blank=True, max_length=500, null=True)),
                ("text_de", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "image",
                    models.ImageField(
                        default="https://via.placeholder.com/400",
                        upload_to="main_page/help_us/",
                    ),
                ),
            ],
        ),
    ]
