# Generated by Django 2.0.3 on 2019-01-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190105_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violation',
            name='compl_per_begin_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
