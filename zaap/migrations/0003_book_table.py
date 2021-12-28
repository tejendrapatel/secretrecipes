# Generated by Django 4.0 on 2021-12-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaap', '0002_testimony_delete_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('time', models.TimeField(null=True)),
                ('persons', models.CharField(max_length=10, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]