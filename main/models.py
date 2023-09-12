from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com o autor (supondo que você está usando o modelo de usuário padrão do Django)
    title = models.CharField(max_length=255)  # Título do post
    description = models.TextField()  # Descrição do post
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação do post (será preenchida automaticamente na criação)
    updated_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do post (será atualizada automaticamente na atualização)

    def __str__(self):
        return self.title  + '\n' + self.description # Representação em string do post (usando o título)