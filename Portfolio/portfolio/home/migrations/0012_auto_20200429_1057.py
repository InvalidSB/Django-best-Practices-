# Generated by Django 3.0.5 on 2020-04-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200429_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestWorkWD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.DeleteModel(
            name='LatestWork',
        ),
    ]