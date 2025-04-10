# Generated by Django 4.2.19 on 2025-02-21 13:46

import InvenTree.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0115_auto_20250221_1323"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockitem",
            name="link",
            field=InvenTree.fields.InvenTreeURLField(
                blank=True,
                help_text="Link to external URL",
                max_length=2000,
                verbose_name="External Link",
            ),
        ),
    ]
