# Generated by Django 3.1.2 on 2020-11-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20201103_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('positions', models.CharField(max_length=50)),
                ('profile', models.TextField(max_length=250)),
                ('avatar_url', models.CharField(max_length=250)),
                ('level', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='website',
            name='cover_img_url',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='website',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='website',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.CharField(max_length=250),
        ),
    ]