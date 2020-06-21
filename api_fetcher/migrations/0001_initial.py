# Generated by Django 3.0.5 on 2020-04-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('imageUrl', models.CharField(max_length=250)),
            ],
        ),
    ]
