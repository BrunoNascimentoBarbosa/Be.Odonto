# Generated by Django 4.1.2 on 2022-10-21 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_delete_comentario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ('nome',)},
        ),
        migrations.CreateModel(
            name='consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historico_consulta', models.TextField(max_length=3000)),
                ('data', models.DateField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consulta', to='paciente.paciente')),
            ],
        ),
    ]
