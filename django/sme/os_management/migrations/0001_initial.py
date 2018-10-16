# Generated by Django 2.0.9 on 2018-10-09 05:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenadoria',
            fields=[
                ('id_coord', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('coord_nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Divisao',
            fields=[
                ('id_divisao', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('divisao_sigla', models.CharField(max_length=6)),
                ('divisao_nome', models.CharField(max_length=100)),
                ('id_coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='os_management.Coordenadoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('usuario_login', models.CharField(max_length=10)),
                ('usuario_nome', models.CharField(max_length=100)),
                ('id_divisao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='os_management.Divisao')),
            ],
        ),
    ]