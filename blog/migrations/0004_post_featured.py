# Generated by Django 4.0.1 on 2022-01-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]