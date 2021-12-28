# Generated by Django 4.0 on 2021-12-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaap', '0005_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_choice', models.CharField(choices=[('cakes', 'cakes'), ('icecream', 'icecream'), ('chinese', 'chinese'), ('indian', 'indian'), ('italian', 'italian')], max_length=30)),
                ('image', models.FileField(null=True, upload_to='')),
                ('name', models.CharField(max_length=50, null=True)),
                ('detail', models.CharField(max_length=500, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]