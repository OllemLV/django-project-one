# Generated by Django 2.1.7 on 2019-03-10 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190309_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='additional_link',
        ),
        migrations.RemoveField(
            model_name='job',
            name='finish_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='title',
        ),
    ]
