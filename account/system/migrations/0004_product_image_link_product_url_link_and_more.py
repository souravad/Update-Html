# Generated by Django 4.2.7 on 2023-11-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_product_options_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_link',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='url_link',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]