# Generated by Django 5.0.1 on 2024-09-05 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_todo_alter_shippinguser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippinguser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='shippinguser',
            name='user_permissions',
        ),
    ]
