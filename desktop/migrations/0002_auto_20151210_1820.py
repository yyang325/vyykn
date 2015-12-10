# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desktop',
            old_name='id',
            new_name='desktop_id',
        ),
    ]
