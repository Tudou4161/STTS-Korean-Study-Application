# Generated by Django 3.1.2 on 2020-10-30 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0002_auto_20201030_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionandanswer',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
