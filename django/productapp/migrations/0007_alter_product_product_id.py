# Generated by Django 3.2.3 on 2021-05-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0006_alter_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
