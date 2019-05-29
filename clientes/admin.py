from django.contrib import admin
from .models import Person
from .models import Documento
from .models import Venda
from .models import Produto

# Criando Actions Personalizadas para o form admim do Django
from .actions_personalizadas import criando_actions_personalizadas_nfe_emitida, criando_actions_personalizadas_nfe_nao_emitida

# Personalizando o Admin do Django
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
class PersonAdmin(admin.ModelAdmin):
    # Personaliza os fields dentro do form do admin (detalhe)
    #fields = ('doc', 'first_name', 'last_name', 'age', 'salary', 'bio', 'photo')

    #Agrupando os campos
    #fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('first_name', 'last_name', 'doc')
        }),
        ('Dados Complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'bio', 'photo')
        }),
        #('Dados Complementares', {'fields': {'age','salary',  'bio', 'photo' }}),
    )
    #Se quisermos excluir algum campo (detalhe)
    #exclude = ['age']

    #Passamos a lista de campos que queremos exibir na lista de todos os Persons
    #list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'photo')

    #Habilitando filtros de campos
    list_filter = ('age', 'salary')

    #Métodos personalizados para list_display
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'tem_foto')

    # Autocomplete - Precisa colocar isso para o autocomplete funcionar no Vendas
    search_fields = ['id', 'first_name']

    def tem_foto(self, obj):
        if obj.photo:
            return 'Tem Foto'
        else:
            return 'Não Tem Foto'

    #criando o short_description
    tem_foto.short_description = 'Possui Foto'



# Adicionado filtros por venda e por cpf, por exemplo
class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'total', 'nfe_emitida')

    # Autocomplete
    autocomplete_fields = ('pessoa',)
    #raw_id_fields = ('pessoa', )


    #readonly_fields = ('desconto', )

    filter_horizontal = ['produtos',]
    #filter_vertical = ['produtos',]

    #habilitando o search field
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')

    # Passando as actions personalizadas criadas
    actions = [
        criando_actions_personalizadas_nfe_emitida,
        criando_actions_personalizadas_nfe_nao_emitida,
    ]

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')

# Personalizando o Admin do Django - Passando a classe
admin.site.register(Person, PersonAdmin)

admin.site.register(Documento)
# Personalizando o Admin do Django - Passando a classe
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)

# Register your models here.
