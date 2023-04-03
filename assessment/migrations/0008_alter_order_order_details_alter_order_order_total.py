# Generated by Django 4.1.7 on 2023-04-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0007_remove_order_order_by_order_user_delete_customeruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_details',
            field=models.JSONField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(blank=True, default=None),
        ),
    ]