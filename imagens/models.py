from django.db import models

class Imagem(models.Model):
    descricao = models.CharField(max_length=30)
    foto = models.ImageField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
