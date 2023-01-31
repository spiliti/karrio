# Generated by Django 3.2.11 on 2022-03-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0029_auto_20220303_1249'),
        ('orders', '0006_alter_order_shipping_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='line_items',
            field=models.ManyToManyField(related_name='commodity_order', through='orders.OrderLineItemLink', to='manager.Commodity'),
        ),
    ]