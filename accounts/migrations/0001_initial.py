# Generated by Django 3.2.25 on 2024-04-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(blank=True, max_length=150)),
                ('body', models.TextField(blank=True)),
                ('image', models.ImageField(default='../profile_kqgeo6.jpg', upload_to='images/')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
