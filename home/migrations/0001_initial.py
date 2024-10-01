# Generated by Django 5.1.1 on 2024-10-01 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('teamname', models.CharField(max_length=50, verbose_name='Team Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('collegename', models.CharField(max_length=50, verbose_name='College Name')),
                ('event', models.CharField(max_length=50, verbose_name='Event Name')),
            ],
        ),
    ]
