# Generated by Django 3.1.2 on 2020-11-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20201103_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/sites/'),
        ),
    ]
