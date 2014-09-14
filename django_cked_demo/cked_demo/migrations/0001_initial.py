# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=100)),
                ('text', models.TextField(verbose_name='Text', max_length=16536)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'articles',
                'verbose_name': 'article',
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
    ]
