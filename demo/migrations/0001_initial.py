# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('message', models.TextField()),
                ('message1', models.TextField(default=None)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
    ]
