# Generated by Django 5.0.3 on 2024-03-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0005_rename_email_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='example@gmail.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='password',
            field=models.CharField(default=12345, max_length=8),
            preserve_default=False,
        ),
    ]
