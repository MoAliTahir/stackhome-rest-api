# Generated by Django 2.2.4 on 2019-11-11 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('id_card', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('full_name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('district', models.CharField(choices=[("M'hannech", "M'hannech"), ('Touta', 'Touta'), ('Martil', 'Martil'), ('Wilaya', 'Wilaya'), ('Saniat Rmel', 'Saniat Rmel'), ('Safir', 'Safir'), ('Soukna w Ta3mir', 'Soukna w Ta3mir'), ('Autre', 'Autre')], max_length=20)),
                ('equipped', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('bedrooms', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('living_room', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('bathroom', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')], default=1)),
                ('price', models.IntegerField(default=0)),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Fridge', 'Fridge'), ('Gas stove', 'Gas stove'), ('Balcony', 'Balcony'), ('Water heater', 'Water heater'), ('Dish washer', 'Dish washer'), ('Washing machine', 'Washing machine'), ('television', 'television'), ('Surveillance camera', 'Surveillance camera'), ('Cooking tools', 'Cooking tools'), ('Oven', 'Oven'), ('Wifi', 'Wifi')], max_length=120)),
                ('description', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('img1', models.FileField(blank=True, upload_to='apartment_pics')),
                ('img2', models.FileField(blank=True, upload_to='apartment_pics')),
                ('img3', models.FileField(blank=True, upload_to='apartment_pics')),
                ('img4', models.FileField(blank=True, upload_to='apartment_pics')),
                ('img5', models.FileField(blank=True, upload_to='apartment_pics')),
                ('img6', models.FileField(blank=True, upload_to='apartment_pics')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('district', models.CharField(choices=[("M'hannech", "M'hannech"), ('Touta', 'Touta'), ('Martil', 'Martil'), ('Wilaya', 'Wilaya'), ('Saniat Rmel', 'Saniat Rmel'), ('Safir', 'Safir'), ('Soukna w Ta3mir', 'Soukna w Ta3mir'), ('Autre', 'Autre')], max_length=20)),
                ('equipped', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('beds', models.IntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Fridge', 'Fridge'), ('Desk', 'Desk'), ('Balcony', 'Balcony'), ('Cabinet', 'Cabinet'), ('Attached bath', 'Attached bath')], max_length=41)),
                ('description', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('img1', models.FileField(blank=True, upload_to='apartment_pics')),
                ('img2', models.FileField(blank=True, upload_to='apartment_pics')),
                ('img3', models.FileField(blank=True, upload_to='apartment_pics')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Ignored')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='stackhome.Apartment')),
                ('room', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='stackhome.Room')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='rents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
