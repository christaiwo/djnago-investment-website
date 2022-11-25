# Generated by Django 4.1.3 on 2022-11-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_earnings_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradings',
            name='active_days',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tradings',
            name='duration',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tradings',
            name='next_day',
            field=models.DateTimeField(max_length=100, null=True),
        ),
    ]
