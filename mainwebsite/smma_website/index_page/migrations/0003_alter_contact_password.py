# Generated by Django 5.0.3 on 2024-03-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0002_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
