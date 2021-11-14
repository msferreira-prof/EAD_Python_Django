from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Categoria, Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
