# Generated by Django 4.1.5 on 2023-01-25 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_comment_post_comments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="comments",
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
        ),
    ]
