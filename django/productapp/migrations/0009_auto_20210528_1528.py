# Generated by Django 3.2.3 on 2021-05-28 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_auto_20210528_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='descriptions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='productapp.categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
