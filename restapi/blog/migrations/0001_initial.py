# Generated by Django 2.2.2 on 2019-06-19 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar', models.ImageField(upload_to='./images')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
            ],
        ),
    ]
