# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('ip_address', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('desktop', models.ForeignKey(to='desktop.DeskTop')),
            ],
        ),
    ]
