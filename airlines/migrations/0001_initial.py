# Generated by Django 3.1.1 on 2020-09-14 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('is_vip', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('seats', models.SmallIntegerField()),
                ('datetime', models.DateTimeField()),
                ('from_city', models.CharField(max_length=32)),
                ('to_city', models.CharField(max_length=32)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='airlines.airline')),
            ],
        ),
    ]
