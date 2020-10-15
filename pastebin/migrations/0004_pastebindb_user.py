# Generated by Django 3.1.2 on 2020-10-14 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pastebin', '0003_remove_pastebindb_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastebindb',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
