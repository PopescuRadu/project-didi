# Generated by Django 4.0.6 on 2022-10-04 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_productproperty_product_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productproperty',
            name='product_fk',
        ),
        migrations.AddField(
            model_name='product',
            name='property_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productproperty'),
        ),
    ]
