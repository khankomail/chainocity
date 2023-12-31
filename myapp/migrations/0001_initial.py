# Generated by Django 4.0.10 on 2023-12-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(max_length=85)),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('p_desc', models.TextField()),
                ('p_stock', models.PositiveIntegerField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
