# Generated by Django 5.0.2 on 2024-02-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Joanne Rowling', max_length=255),
            preserve_default=False,
        ),
    ]