# Generated by Django 5.0 on 2024-01-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_order_payment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
