# Generated by Django 4.2.13 on 2024-06-07 22:05

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pages_written', models.IntegerField()),
                ('authors', models.ManyToManyField(to='booklist.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booklist.publisher')),
            ],
        ),
    ]
