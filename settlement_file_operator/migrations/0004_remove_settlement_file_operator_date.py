# Generated by Django 3.2.9 on 2022-07-27 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settlement_file_operator', '0003_alter_settlement_file_operator_cooperatives'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settlement_file_operator',
            name='date',
        ),
    ]