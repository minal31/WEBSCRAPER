# Generated by Django 3.1 on 2021-05-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='web',
            name='hrefvalue',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='linkname',
            field=models.CharField(max_length=60, null=True),
        ),
    ]