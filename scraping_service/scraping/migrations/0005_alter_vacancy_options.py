# Generated by Django 3.2.4 on 2021-07-14 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]