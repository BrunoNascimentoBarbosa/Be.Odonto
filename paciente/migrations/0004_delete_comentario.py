# Generated by Django 4.1.2 on 2022-10-21 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_alter_comentario_nome_paciente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comentario',
        ),
    ]
