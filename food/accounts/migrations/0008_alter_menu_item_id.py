# Generated by Django 5.1.3 on 2024-12-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_menu_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Item_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
