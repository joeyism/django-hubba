# Generated by Django 2.0 on 2018-01-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=512),
        ),
    ]
