# Generated by Django 3.2.8 on 2022-02-28 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_reply_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to='comments.comment'),
        ),
    ]