# Generated by Django 5.1.2 on 2024-11-13 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_remove_investigator_bio_investigator_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='markdown',
        ),
        migrations.RemoveField(
            model_name='investigator',
            name='superhero',
        ),
        migrations.AddField(
            model_name='article',
            name='hero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='hero.superhero'),
        ),
        migrations.AddField(
            model_name='article',
            name='html',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='superhero',
            name='investigator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='superheroes', to='hero.investigator'),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.ImageField(blank=True, default='superheroes/default_image.jpg', upload_to='superheroes/'),
            preserve_default=False,
        ),
    ]