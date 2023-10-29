# Generated by Django 4.1 on 2023-10-18 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0005_comment_timestamp_like_timestamp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="like",
            old_name="created_by",
            new_name="liked_by",
        ),
        migrations.AddField(
            model_name="comment",
            name="count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="like",
            name="count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="commented",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
