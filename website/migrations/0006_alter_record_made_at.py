# Generated by Django 4.2.4 on 2023-08-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_record_made_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='made_at',
            field=models.DateTimeField(),
        ),
    ]
