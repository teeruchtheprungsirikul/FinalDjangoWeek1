# Generated by Django 4.1.1 on 2022-09-25 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cover'),
        ),
    ]
