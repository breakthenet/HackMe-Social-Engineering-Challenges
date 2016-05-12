# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_emailattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailattachment',
            name='name',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
