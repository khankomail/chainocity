# Generated by Django 5.0 on 2024-01-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_order_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='img3',
            field=models.ImageField(blank=True, default='defaultUser.jpg', null=True, upload_to=''),
        ),
    ]
