from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from core.models import Genero, Desenvolvedora, Plataforma, Jogo, Compra, ItensCompra


class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class DesenvolvedoraSerializer(ModelSerializer):
    class Meta:
        model = Desenvolvedora
        fields = '__all__'


class DesenvolvedoraNestedSerializer(ModelSerializer):
    class Meta:
        model = Desenvolvedora
        fields = ['nome']

        
class PlataformaSerializer(ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'
        

class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'
        

class JogoDetailSerializer(ModelSerializer):
    genero = CharField(source="genero.descricao")
    desenvolvedora = DesenvolvedoraNestedSerializer()
    plataforma = SerializerMethodField()
    
    class Meta:
        model = Jogo
        fields = '__all__'
        depth = 1
        
    def get_plataforma(self, instance):
        nomes_plataformas = []
        plataformas = instance.plataforma.get_queryset()
        for plataforma in plataformas:
            nomes_plataformas.append(plataforma.nome)
        return nomes_plataformas


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    
    class Meta:
        model = ItensCompra
        fields = ['jogo', 'quantidade', 'total']
        depth = 2
    
    def get_total(self, instance):
        return instance.quantidade * instance.jogo.preco
    

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ['jogo', 'quantidade']


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email")
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many=True)
    
    class Meta:
        model = Compra
        fields = ['id', 'status', 'usuario', 'itens', 'total']
        
    def get_status(self, instance):
        return instance.get_status_display()
    

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    
    class Meta:
        model = Compra
        fields = ['usuario', 'itens']
        
    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
    
    def update(self, instance, validated_data):
        itens = validated_data.pop('itens')
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
        return instance