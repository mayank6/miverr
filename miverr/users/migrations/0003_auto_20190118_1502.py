# Generated by Django 2.1.5 on 2019-01-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190117_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.CharField(default='xyz', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.CharField(default='xyz', max_length=500),
            preserve_default=False,
        ),
    ]