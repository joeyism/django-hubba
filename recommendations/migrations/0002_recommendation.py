# Generated by Django 2.0 on 2018-01-19 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32)),
                ('context_product', models.CharField(max_length=128)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recommendations.Buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recommendations.Product')),
            ],
        ),
    ]