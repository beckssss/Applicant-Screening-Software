# Generated by Django 2.1.7 on 2019-04-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_status_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='bb', max_length=100),
        ),
    ]
