# Generated by Django 5.1.5 on 2025-02-04 14:21

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('category', models.CharField(choices=[('TNK', 'Танки'), ('HIL', 'Хилы'), ('DD', 'ДД'), ('MER', 'Торговцы'), ('GUD', 'Гилдмастеры'), ('QUS', 'Квестгиверы'), ('BLC', 'Кузнецы'), ('TNR', 'Кожевники'), ('PBR', 'Зельевары'), ('SPM', 'Мастера заклинаний')], default='TNK', max_length=3)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Активное'), ('INACTIVE', 'Неактивное'), ('COMPLETED', 'Завершено')], default='ACTIVE', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ACP', 'Принято'), ('REJ', 'Отклонено'), ('EXP', 'Ожидание')], default='EXP', max_length=3)),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.announcement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
