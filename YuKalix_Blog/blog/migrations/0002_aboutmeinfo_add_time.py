# Generated by Django 2.0 on 2019-02-19 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmeinfo',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='时间'),
            preserve_default=False,
        ),
    ]
