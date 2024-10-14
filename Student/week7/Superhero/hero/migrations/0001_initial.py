# Generated by Django 5.1.1 on 2024-10-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('identity', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=200)),
                ('strengths', models.CharField(max_length=200)),
                ('weaknesses', models.CharField(max_length=200)),
            ],
        ),
    ]
