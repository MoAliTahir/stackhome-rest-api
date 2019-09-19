# Generated by Django 2.2.4 on 2019-09-18 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('equipped', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('bedrooms', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('living_room', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('bathroom', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')], default=1)),
                ('price', models.IntegerField(default=0)),
                ('features', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
