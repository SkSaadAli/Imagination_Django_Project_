# Generated by Django 3.2.9 on 2023-01-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
