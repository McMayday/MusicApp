# Generated by Django 3.1.5 on 2021-01-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210110_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guest_can_pause',
            field=models.BooleanField(default=False, null=True),
        ),
    ]