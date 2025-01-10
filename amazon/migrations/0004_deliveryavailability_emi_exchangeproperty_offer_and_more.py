# Generated by Django 4.2.16 on 2025-01-10 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("amazon", "0003_itemview"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryAvailability",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("can_receive_on_saturday", models.BooleanField()),
                ("can_receive_on_sunday", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Emi",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("emi_type", models.CharField(max_length=255)),
                ("emi_amount", models.FloatField()),
                ("card_name", models.CharField(blank=True, max_length=255, null=True)),
                ("processing_fee", models.FloatField(blank=True, null=True)),
                ("minimum_purchase_value", models.FloatField(blank=True, null=True)),
                ("number_of_months", models.IntegerField()),
                ("intereset_in_rupees", models.FloatField()),
                ("interest_in_percentage", models.FloatField()),
                ("discount_in_rupees", models.FloatField(blank=True, null=True)),
                ("total_amount", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="ExchangeProperty",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exchange_property_name",
                    models.CharField(max_length=255, unique=True),
                ),
                (
                    "exchange_property_value",
                    models.CharField(max_length=255, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("offer_type", models.CharField(max_length=255)),
                ("offer_name", models.CharField(blank=True, max_length=255, null=True)),
                ("card_name", models.CharField(blank=True, max_length=255, null=True)),
                ("discount_in_rupees", models.FloatField()),
                ("discount_in_percentage", models.FloatField()),
                ("minimum_purchase_value", models.FloatField(blank=True, null=True)),
                ("minimum_months_emi", models.IntegerField(blank=True, null=True)),
                (
                    "coupoun_code",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("minimum_number_of_items", models.IntegerField(blank=True, null=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("terms_and_conditions", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Warranty",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("warranty_name", models.CharField(max_length=255, unique=True)),
                ("number_fo_years", models.IntegerField()),
                ("warranty_description", models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="cart",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="amazon.cart",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="delivery_charges",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="receiving_person_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="ItemWarranty",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itemwarranty",
                        to="amazon.item",
                    ),
                ),
                (
                    "warranty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itemwarranty",
                        to="amazon.warranty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemOffer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itemoffers",
                        to="amazon.item",
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itemoffers",
                        to="amazon.offer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemExchangeProperty",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exchangeproperty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itemexchangeproperty",
                        to="amazon.exchangeproperty",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itemexchangeproperty",
                        to="amazon.item",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemEmi",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "emi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itememi",
                        to="amazon.emi",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itememi",
                        to="amazon.item",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExchangeValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("exchange_value", models.FloatField()),
                ("exchange_service_fee", models.FloatField()),
                (
                    "exchangeproperties",
                    models.ManyToManyField(
                        related_name="exchangevalues", to="amazon.exchangeproperty"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="emis",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="items",
                through="amazon.ItemEmi",
                to="amazon.emi",
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="exchangeproperties",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="items",
                through="amazon.ItemExchangeProperty",
                to="amazon.exchangeproperty",
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="offers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="items",
                through="amazon.ItemOffer",
                to="amazon.offer",
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="warranties",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="items",
                through="amazon.ItemWarranty",
                to="amazon.warranty",
            ),
        ),
        migrations.AddField(
            model_name="itemscart",
            name="itemexchangeproperties",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="itemscart",
                to="amazon.itemexchangeproperty",
            ),
        ),
        migrations.AddField(
            model_name="itemscart",
            name="itemwarranty",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="itemscart",
                to="amazon.itemwarranty",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="delivery_availability",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="amazon.deliveryavailability",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="itemwarranty",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="amazon.itemwarranty",
            ),
        ),
    ]
