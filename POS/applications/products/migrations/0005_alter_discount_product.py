# Generated by Django 4.1 on 2022-08-22 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_original_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discount",
                to="products.product",
            ),
        ),
    ]
