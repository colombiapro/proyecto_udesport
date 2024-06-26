# Generated by Django 5.0.4 on 2024-04-11 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('idDeporte', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre_dep', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ev', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('codigo', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('edad', models.IntegerField(null=True)),
                ('sexo', models.CharField(max_length=1, null=True)),
                ('tipo', models.CharField(max_length=1, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('seleccion', models.CharField(blank=True, max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('programa', models.CharField(blank=True, max_length=60, null=True)),
                ('semestre', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Usuario',
                'db_table_comment': 'Contiene la informaci�n  de los usuarios registrados ',
            },
        ),
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('idCampeonato', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=1)),
                ('fecha_inicio', models.DateField()),
                ('idDeporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Desafios',
            fields=[
                ('idDesafio', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('equipo1', models.CharField(max_length=50)),
                ('equipo2', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('lugar', models.CharField(max_length=100)),
                ('ganador', models.CharField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('idEquipo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre_eq', models.CharField(max_length=50)),
                ('num_integrantes', models.IntegerField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.campeonato')),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Rendimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.IntegerField(null=True)),
                ('campo2', models.IntegerField(null=True)),
                ('campo3', models.IntegerField(null=True)),
                ('campo4', models.IntegerField(null=True)),
                ('campo5', models.IntegerField(null=True)),
                ('grasa_corporal', models.IntegerField(null=True)),
                ('masa_muscular', models.IntegerField(null=True)),
                ('rendimiento', models.IntegerField(null=True)),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.deporte')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
