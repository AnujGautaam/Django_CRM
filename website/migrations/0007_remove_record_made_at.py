# Generated by Django 4.2.4 on 2023-08-22 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_record_made_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='made_at',
        ),
    ]
