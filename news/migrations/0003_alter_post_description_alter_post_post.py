# Generated by Django 5.0.6 on 2024-06-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_category_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(),
        ),
    ]