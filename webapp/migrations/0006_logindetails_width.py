# Generated by Django 4.2.5 on 2024-02-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_logindetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindetails',
            name='width',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
