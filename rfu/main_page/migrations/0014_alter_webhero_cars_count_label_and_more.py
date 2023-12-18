# Generated by Django 4.1.7 on 2023-12-17 00:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0013_alter_webhero_options_webhero_cars_count_label_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_de",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_en",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_pl",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_ru",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="cars_count_label_ua",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_rfu_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_rfu_label_de",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_rfu_label_en",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_rfu_label_pl",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_rfu_label_ru",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_rfu_label_ua",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_war_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_war_label_de",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_war_label_en",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_war_label_pl",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_war_label_ru",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="days_of_war_label_ua",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="flights_count_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="flights_count_label_de",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="flights_count_label_en",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="flights_count_label_pl",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="flights_count_label_ru",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="flights_count_label_ua",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="humanitarian_goods_weight_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="humanitarian_goods_weight_label_de",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="humanitarian_goods_weight_label_en",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="humanitarian_goods_weight_label_pl",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="humanitarian_goods_weight_label_ru",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="humanitarian_goods_weight_label_ua",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="shelter_refugees_count_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="shelter_refugees_count_label_de",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="shelter_refugees_count_label_en",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="shelter_refugees_count_label_pl",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="shelter_refugees_count_label_ru",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="shelter_refugees_count_label_ua",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="volunteers_count_label",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="volunteers_count_label_de",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="volunteers_count_label_en",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="volunteers_count_label_pl",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="volunteers_count_label_ru",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="volunteers_count_label_ua",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
