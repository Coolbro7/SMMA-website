# Generated by Django 5.0.3 on 2024-03-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0007_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='reason',
            field=models.CharField(default='rijan', max_length=65535),
            preserve_default=False,
        ),
    ]
