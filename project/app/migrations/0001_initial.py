# Generated by Django 5.0 on 2023-12-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'chel',
                'verbose_name_plural': 'люди',
            },
        ),
    ]
