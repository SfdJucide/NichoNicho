# Generated by Django 4.2 on 2023-05-01 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('short_description', models.TextField(blank=True, verbose_name='Описание')),
                ('long_description', models.TextField(blank=True)),
                ('available', models.BooleanField(default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Пользователь')),
                ('register_date', models.DateTimeField(auto_now=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'TG Пользователь',
                'verbose_name_plural': 'TG Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products', verbose_name='Картинка')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tgcore.product')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='tgcore.tguser')),
            ],
        ),
    ]
