from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):
    STATUS =(
        ('pendente','Pendente'),
        ('concluido','Concluido'),
    )
    PRECO = (
        ('R$250,00', 'R$250,00'),
        ('R$150,00', 'R$150,00'),
    )
    SERVICO_TIPO = (
        ('limpeza profunda', 'Limpeza Profunda'),
        ('limpeza simples', 'Limpeza Simples'),
    )

    cliente = models.CharField(max_length=255)
    Serviço = models.CharField(
        max_length=100,
        choices=SERVICO_TIPO,
    )
    preço = models.CharField(
        max_length=100,
        choices=PRECO,
    )
    atendente = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    data_atendimento = models.CharField(max_length=255)
    data_limpeza = models.CharField(max_length=255)
    obs = models.TextField()
    done = models.CharField(
        max_length=100,
        choices = STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cliente