# Generated by Django 5.0.2 on 2024-03-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_special_delete_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='special',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
