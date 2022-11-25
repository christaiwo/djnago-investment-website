# Generated by Django 4.1.3 on 2022-11-23 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_remove_tradings_plan_id_tradings_trading_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routing_no', models.CharField(max_length=30, null=True)),
                ('bank_name', models.CharField(max_length=100, null=True)),
                ('account_no', models.CharField(max_length=30, null=True)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(default=0, max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bank',
            },
        ),
    ]
