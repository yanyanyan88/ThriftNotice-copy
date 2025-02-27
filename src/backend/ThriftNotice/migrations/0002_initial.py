# Generated by Django 5.1.6 on 2025-02-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ThriftNotice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThriftStores',
            fields=[
                ('shopid', models.BigAutoField(db_column='ShopID', primary_key=True, serialize=False)),
                ('shopname', models.CharField(db_column='ShopName')),
                ('formattedaddress', models.TextField(blank=True, db_column='FormattedAddress', null=True)),
                ('latitude', models.FloatField(blank=True, db_column='Latitude', null=True)),
                ('longitude', models.FloatField(blank=True, db_column='Longitude', null=True)),
                ('shortdescription', models.TextField(blank=True, db_column='ShortDescription', null=True)),
                ('pricerange', models.TextField(blank=True, db_column='PriceRange', null=True)),
                ('specialty', models.TextField(blank=True, db_column='Specialty', null=True)),
                ('isestablishedstore', models.BinaryField(blank=True, db_column='IsEstablishedStore', null=True)),
                ('popupstarttime', models.DateTimeField(blank=True, db_column='PopUpStartTime', null=True)),
                ('hasfittingrooms', models.BooleanField(blank=True, db_column='HasFittingRooms', null=True)),
                ('parkingavailability', models.TextField(blank=True, db_column='ParkingAvailability', null=True)),
                ('ispopupevent', models.BooleanField(blank=True, db_column='IsPopUpEvent', null=True)),
            ],
            options={
                'db_table': 'thrift_stores',
                'db_table_comment': 'A Relation Containing Information Of Each Thrift Shop',
                'managed': False,
            },
        ),
    ]
