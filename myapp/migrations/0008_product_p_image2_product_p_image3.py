# Generated by Django 5.0 on 2023-12-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_profilepic_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_image2',
            field=models.ImageField(blank=True, default='default_p.jpg', null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='p_image3',
            field=models.ImageField(blank=True, default='default_p.jpg', null=True, upload_to='product_images/'),
        ),
    ]
