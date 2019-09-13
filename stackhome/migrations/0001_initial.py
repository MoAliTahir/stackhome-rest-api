# Generated by Django 2.2.4 on 2019-09-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('equipped', models.BooleanField(default=False)),
                ('bedrooms', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('living_room', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('bathroom', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')], default=1)),
                ('price', models.IntegerField(default=0)),
                ('features', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]