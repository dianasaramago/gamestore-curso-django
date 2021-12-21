from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class Genero(models.Model):
    class Meta:
        verbose_name_plural = "gêneros"
        
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.descricao


class Desenvolvedora(models.Model):
    class Meta:
        verbose_name_plural = "desenvolvedoras"
        
    nome = models.CharField(max_length=255)
    site = models.URLField()
    
    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    class Meta:
        verbose_name_plural = "plataformas"
        
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    

class Jogo(models.Model):
    class Meta:
        verbose_name_plural = "jogos"
        
    titulo = models.CharField(max_length=255)
    ano = models.IntegerField()
    resumo = models.TextField(max_length=1000)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name="jogos")
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.PROTECT, related_name="jogos")
    plataforma = models.ManyToManyField(Plataforma, related_name="jogos")
    
    def __str__(self):
        return "%s (%s)" %(self.titulo, self.desenvolvedora)
    

class Compra(models.Model):
    
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'
        
        
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    
    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total = models.Sum(F('quantidade') * F('jogo__preco'))
            )
        return queryset['total']


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()