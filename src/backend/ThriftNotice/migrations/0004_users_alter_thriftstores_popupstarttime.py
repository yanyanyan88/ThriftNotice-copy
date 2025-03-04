# Generated by Django 5.1.6 on 2025-02-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThriftNotice', '0003_alter_thriftstores_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.BigAutoField(db_column='userid', primary_key=True, serialize=False)),
                ('clothing', models.TextField(db_column='clothing')),
                ('shoppingenvironment', models.TextField(db_column='shoppingenvironment')),
                ('budget', models.FloatField(db_column='budget')),
                ('organization', models.TextField(db_column='organization')),
                ('interest', models.TextField(db_column='interest')),
            ],
        ),
        migrations.AlterField(
            model_name='thriftstores',
            name='popupstarttime',
            field=models.TimeField(blank=True, db_column='PopUpStartTime', null=True),
        ),
    ]
