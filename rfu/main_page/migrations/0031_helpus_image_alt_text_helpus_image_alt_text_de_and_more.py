# Generated by Django 4.1.7 on 2023-12-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0030_mission_image_alt_text_mission_image_alt_text_de_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="helpus",
            name="image_alt_text",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="helpus",
            name="image_alt_text_de",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="helpus",
            name="image_alt_text_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="helpus",
            name="image_alt_text_pl",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="helpus",
            name="image_alt_text_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="helpus",
            name="image_alt_text_ua",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="modalwindow",
            name="image_alt_text",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="modalwindow",
            name="image_alt_text_de",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="modalwindow",
            name="image_alt_text_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="modalwindow",
            name="image_alt_text_pl",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="modalwindow",
            name="image_alt_text_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="modalwindow",
            name="image_alt_text_ua",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="ourwork",
            name="image_alt_text",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="ourwork",
            name="image_alt_text_de",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="ourwork",
            name="image_alt_text_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="ourwork",
            name="image_alt_text_pl",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="ourwork",
            name="image_alt_text_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="ourwork",
            name="image_alt_text_ua",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="image_alt_text",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="image_alt_text_de",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="image_alt_text_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="image_alt_text_pl",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="image_alt_text_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="image_alt_text_ua",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
