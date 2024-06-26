# Generated by Django 5.0.3 on 2024-05-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0033_userprofile_default_mark_unread"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmark",
            name="preview_image_file",
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="enable_preview_images",
            field=models.BooleanField(default=False),
        ),
    ]
