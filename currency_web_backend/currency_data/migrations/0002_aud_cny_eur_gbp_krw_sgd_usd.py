# Generated by Django 2.1.2 on 2018-12-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AUD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_cash_buy', models.FloatField()),
                ('rate_cash_sell', models.FloatField()),
                ('rate_sight_buy', models.FloatField()),
                ('rate_sight_sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CNY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_cash_buy', models.FloatField()),
                ('rate_cash_sell', models.FloatField()),
                ('rate_sight_buy', models.FloatField()),
                ('rate_sight_sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EUR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_cash_buy', models.FloatField()),
                ('rate_cash_sell', models.FloatField()),
                ('rate_sight_buy', models.FloatField()),
                ('rate_sight_sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GBP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_cash_buy', models.FloatField()),
                ('rate_cash_sell', models.FloatField()),
                ('rate_sight_buy', models.FloatField()),
                ('rate_sight_sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='KRW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_cash_buy', models.FloatField()),
                ('rate_cash_sell', models.FloatField()),
                ('rate_sight_buy', models.FloatField()),
                ('rate_sight_sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SGD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_cash_buy', models.FloatField()),
                ('rate_cash_sell', models.FloatField()),
                ('rate_sight_buy', models.FloatField()),
                ('rate_sight_sell', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='USD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate_cash_buy', models.FloatField()),
                ('rate_cash_sell', models.FloatField()),
                ('rate_sight_buy', models.FloatField()),
                ('rate_sight_sell', models.FloatField()),
            ],
        ),
    ]