# Generated by Django 4.0.3 on 2022-03-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quanntity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
