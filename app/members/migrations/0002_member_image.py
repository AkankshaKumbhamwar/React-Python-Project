# Generated by Django 5.0 on 2023-12-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='member_images/'),
        ),
    ]
