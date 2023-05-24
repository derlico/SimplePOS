# Generated by Django 4.2.1 on 2023-05-19 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('product_code', models.IntegerField(verbose_name='Product Code')),
                ('product_price', models.PositiveBigIntegerField(verbose_name='Price')),
                ('product_cost', models.PositiveBigIntegerField(verbose_name='Cost')),
            ],
        ),
    ]
