# Generated by Django 4.1.3 on 2022-11-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_tradings_active_days_alter_tradings_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradings',
            name='active_days',
            field=models.IntegerField(null=True),
        ),
    ]
