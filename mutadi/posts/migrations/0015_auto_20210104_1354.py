# Generated by Django 3.1.5 on 2021-01-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
