# Generated by Django 4.2.4 on 2023-08-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_created_at_record_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='created',
        ),
        migrations.AddField(
            model_name='record',
            name='made_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-08-22 12:08'),
            preserve_default=False,
        ),
    ]