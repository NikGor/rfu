# Generated by Django 4.1.7 on 2023-10-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0002_mission_paymentmethod_socialnetwork"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="webhero",
            name="button",
        ),
        migrations.RemoveField(
            model_name="webhero",
            name="mission",
        ),
        migrations.AlterField(
            model_name="card",
            name="button",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="card",
            name="image",
            field=models.ImageField(
                default="https://via.placeholder.com/400", upload_to="cards/"
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
                    ("bi-currency-bitcoin", "Bitcoin"),
                    ("bi-currency-ethereum", "ETH"),
                    ("bi-cash", "USDT (TRC20)"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="socialnetwork",
            name="icon",
            field=models.CharField(
                blank=True,
                choices=[
                    ("bi-facebook", "Facebook"),
                    ("bi-twitter", "Twitter"),
                    ("bi-telegram", "Telegram"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="webhero",
            name="image",
            field=models.ImageField(
                default="https://via.placeholder.com/2400x800", upload_to="web_hero/"
            ),
        ),
    ]
