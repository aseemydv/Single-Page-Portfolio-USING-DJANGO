# Generated by Django 2.0.4 on 2018-05-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onePgFolio', '0004_auto_20180507_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get_feedback',
            name='email',
            field=models.EmailField(max_length=40),
        ),
    ]
