# Generated by Django 4.1.3 on 2022-11-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_bank_account_name_alter_bank_account_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='status',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
