# Generated by Django 5.1.4 on 2024-12-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_lis', models.CharField(max_length=100)),
                ('product_detail', models.DateField(auto_now_add=True)),
                ('product_create', models.CharField(max_length=100)),
                ('about_page', models.TextField()),
            ],
        ),
    ]