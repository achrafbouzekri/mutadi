# Generated by Django 3.1.4 on 2020-12-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20201220_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]