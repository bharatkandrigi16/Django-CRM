# Generated by Django 4.2.4 on 2023-08-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_messageindex_remove_message_messageindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='messageIndex',
            field=models.IntegerField(default=1),
        ),
    ]
