# Generated by Django 3.0.7 on 2020-06-18 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stokkapp', '0003_auto_20200618_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlistitem',
            old_name='item_id',
            new_name='item',
        ),
    ]
