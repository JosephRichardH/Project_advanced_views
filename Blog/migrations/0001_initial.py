# Generated by Django 2.1.5 on 2019-02-13 04:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postingan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('teks', models.TextField(max_length=225)),
                ('tanggal_dibuat', models.DateField(default=datetime.date(2019, 2, 13))),
            ],
        ),
    ]
