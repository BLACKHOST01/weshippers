# Generated by Django 5.0.1 on 2024-09-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_shippinguser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='tracking_number',
            field=models.CharField(default='0046908928', editable=False, max_length=10, unique=True),
        ),
    ]
