# Generated by Django 4.0.2 on 2022-02-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0003_records_delete_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='is_cropped',
            field=models.BooleanField(default=False),
        ),
    ]