# Generated by Django 3.1.2 on 2020-11-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_remove_website_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='cover_img',
            field=models.ImageField(null=True, upload_to='images/sites/'),
        ),
    ]
