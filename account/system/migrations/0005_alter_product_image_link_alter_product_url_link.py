# Generated by Django 4.2.7 on 2023-11-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_product_image_link_product_url_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='url_link',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
