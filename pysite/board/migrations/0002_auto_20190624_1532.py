# Generated by Django 2.2.2 on 2019-06-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='depth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='board',
            name='group_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='board',
            name='order_no',
            field=models.IntegerField(default=0),
        ),
    ]