# Generated by Django 3.2.11 on 2022-02-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_shopuser_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='город'),
        ),
    ]
