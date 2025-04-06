# Generated by Django 5.1.7 on 2025-04-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_party_candidate_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='Department',
            new_name='department',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
