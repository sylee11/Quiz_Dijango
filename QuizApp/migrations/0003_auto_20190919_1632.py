# Generated by Django 2.1.12 on 2019-09-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0002_auto_20190919_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='anser',
            field=models.IntegerField(),
        ),
    ]
