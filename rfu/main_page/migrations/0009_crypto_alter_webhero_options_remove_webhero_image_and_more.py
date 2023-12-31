# Generated by Django 4.1.7 on 2023-11-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0008_remove_card_description_text_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Crypto",
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
                (
                    "icon",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("bi-currency-bitcoin", "Bitcoin"),
                            ("bi-currency-ethereum", "ETH"),
                            ("bi-cash", "USDT (TRC20)"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="webhero",
            options={"verbose_name": "Web Hero", "verbose_name_plural": "Web Heroes"},
        ),
        migrations.RemoveField(
            model_name="webhero",
            name="image",
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="image",
            field=models.ImageField(
                default="https://via.placeholder.com/150x50",
                upload_to="payment_methods/",
            ),
        ),
        migrations.AddField(
            model_name="webhero",
            name="cars_count",
            field=models.CharField(
                blank=True, default=350, max_length=50, null=True, verbose_name="Машин"
            ),
        ),
        migrations.AddField(
            model_name="webhero",
            name="days_of_rfu",
            field=models.IntegerField(blank=True, null=True, verbose_name="Дней RFU"),
        ),
        migrations.AddField(
            model_name="webhero",
            name="days_of_war",
            field=models.IntegerField(blank=True, null=True, verbose_name="Дней войны"),
        ),
        migrations.AddField(
            model_name="webhero",
            name="flights_count",
            field=models.IntegerField(
                blank=True, default=92, null=True, verbose_name="Рейсы"
            ),
        ),
        migrations.AddField(
            model_name="webhero",
            name="humanitarian_goods_weight",
            field=models.CharField(
                blank=True,
                default=50,
                max_length=50,
                null=True,
                verbose_name="Гуманитарных грузов",
            ),
        ),
        migrations.AddField(
            model_name="webhero",
            name="shelter_refugees_count",
            field=models.CharField(
                blank=True,
                default="2600",
                max_length=50,
                null=True,
                verbose_name="Беженцев в шелтере",
            ),
        ),
        migrations.AddField(
            model_name="webhero",
            name="volunteers_count",
            field=models.IntegerField(
                blank=True, default=320, null=True, verbose_name="Волонтеров"
            ),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="icon",
            field=models.CharField(
                blank=True,
                choices=[
                    ("bi-wallet2", "Wallet"),
                    ("bi-paypal", "Paypal"),
                    ("bi-heart", "GoFundMe"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
