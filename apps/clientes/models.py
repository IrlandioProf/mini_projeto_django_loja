from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
