# Generated by Django 3.0.8 on 2023-11-19 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_ALTERED_also_tryin_todeluserid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_id',
        ),
    ]