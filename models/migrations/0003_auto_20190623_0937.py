# Generated by Django 2.2.2 on 2019-06-23 09:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mark',
            field=models.ManyToManyField(related_name='mark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]
