# Generated by Django 4.0.6 on 2022-12-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='re_password',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
