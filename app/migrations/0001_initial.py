# Generated by Django 4.2.10 on 2024-03-20 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kunlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sinf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan1', models.CharField(max_length=200)),
                ('fan2', models.CharField(max_length=200)),
                ('fan3', models.CharField(max_length=200)),
                ('fan4', models.CharField(max_length=200)),
                ('fan5', models.CharField(max_length=200)),
                ('fan6', models.CharField(max_length=200, null=True)),
                ('kun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kunlar')),
                ('sinf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sinf')),
            ],
        ),
    ]
