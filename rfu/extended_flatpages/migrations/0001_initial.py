# Generated by Django 4.1.7 on 2023-12-08 19:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("flatpages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RichTextFlatPage",
            fields=[
                (
                    "flatpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="flatpages.flatpage",
                    ),
                ),
                ("rich_content", ckeditor.fields.RichTextField()),
            ],
            bases=("flatpages.flatpage",),
        ),
    ]
