# Generated by Django 2.0.3 on 2019-01-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190105_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('gw_sw_code', models.CharField(max_length=200)),
                ('population_served_count', models.IntegerField(default=0)),
                ('pwsid', models.CharField(max_length=200)),
                ('pws_activity_code', models.CharField(max_length=200)),
                ('pws_name', models.CharField(max_length=200)),
                ('state_code', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
                ('counties_served', models.CharField(max_length=200)),
                ('cities_served', models.CharField(max_length=200)),
                ('pws_type_code', models.CharField(blank=True, max_length=6, null=True)),
                ('primacy_agency_code', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]
