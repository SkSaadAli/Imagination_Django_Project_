# Generated by Django 3.2.9 on 2023-01-22 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20230118_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poetry',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
