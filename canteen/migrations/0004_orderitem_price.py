# Generated by Django 3.0.2 on 2020-02-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0003_auto_20200206_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
