# Generated by Django 4.1.6 on 2023-02-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_category_options_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
