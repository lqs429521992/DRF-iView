# Generated by Django 3.0.7 on 2020-08-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinson', '0002_auto_20200730_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=1)),
                ('profession', models.CharField(max_length=20)),
                ('golds', models.IntegerField(default=0)),
                ('diamonds', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]