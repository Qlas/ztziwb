# Generated by Django 3.2.11 on 2022-01-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20220117_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
