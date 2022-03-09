# Generated by Django 3.2.9 on 2022-03-09 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CSVS', '0003_auto_20220307_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_login',
            name='device_type',
            field=models.CharField(choices=[(1, 'mobile'), (2, 'tablet'), (3, 'pc'), (4, 'touch capable'), (5, 'bot')], max_length=200, null=True, verbose_name='Tipo de Dispositivo'),
        ),
    ]