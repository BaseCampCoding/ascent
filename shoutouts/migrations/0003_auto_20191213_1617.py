# Generated by Django 3.0 on 2019-12-13 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoutouts', '0002_auto_20191213_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoutout',
            options={'ordering': ['-datetime']},
        ),
        migrations.AddField(
            model_name='shoutout',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
