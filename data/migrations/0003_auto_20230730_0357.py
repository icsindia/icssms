# Generated by Django 3.2.18 on 2023-07-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='fees',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='fees',
            name='paidamount',
            field=models.IntegerField(),
        ),
    ]
