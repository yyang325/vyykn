# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeskTop',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
