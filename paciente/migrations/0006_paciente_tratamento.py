# Generated by Django 4.1.2 on 2022-10-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_alter_paciente_options_consulta'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='tratamento',
            field=models.CharField(blank=True, choices=[('A', 'Em andamento'), ('P', 'Parado'), ('c', 'Concluído')], max_length=1),
        ),
    ]
