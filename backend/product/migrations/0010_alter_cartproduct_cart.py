# Generated by Django 3.2.11 on 2022-01-18 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_cart_cartproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='product.cart'),
        ),
    ]
