# Generated by Django 4.0.3 on 2022-04-09 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=255)),
                ('Serviço', models.CharField(choices=[('limpeza profunda', 'Limpeza Profunda'), ('limpeza simples', 'Limpeza Simples')], max_length=100)),
                ('preço', models.CharField(choices=[('R$250,00', 'R$250,00'), ('R$150,00', 'R$150,00')], max_length=100)),
                ('atendente', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('data_atendimento', models.CharField(max_length=255)),
                ('data_limpeza', models.CharField(max_length=255)),
                ('obs', models.TextField()),
                ('done', models.CharField(choices=[('pendente', 'Pendente'), ('concluido', 'Concluido')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
