# Generated by Django 2.2.5 on 2019-09-18 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190917_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
