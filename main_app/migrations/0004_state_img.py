# Generated by Django 4.0.2 on 2022-02-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='img',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]
