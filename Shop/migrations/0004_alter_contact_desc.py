# Generated by Django 3.2.8 on 2021-11-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=122),
        ),
    ]
