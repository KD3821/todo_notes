# Generated by Django 3.2.4 on 2021-07-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210708_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='send_email',
            field=models.BooleanField(default=False),
        ),
    ]
