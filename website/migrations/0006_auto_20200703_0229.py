# Generated by Django 2.0.7 on 2020-07-02 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200703_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
