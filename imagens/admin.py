from django.contrib import admin
from imagens.models import Imagem

class ListandoImagens(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'foto', 'data')
    list_display_link = ('id', 'descricao')

admin.site.register(Imagem, ListandoImagens)


