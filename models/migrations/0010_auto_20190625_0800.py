# Generated by Django 2.2.2 on 2019-06-25 08:00

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_auto_20190625_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
