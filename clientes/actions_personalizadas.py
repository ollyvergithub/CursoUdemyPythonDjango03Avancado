def criando_actions_personalizadas_nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)
criando_actions_personalizadas_nfe_emitida.short_description = "Action Personalizada - Nfe Emitida"

def criando_actions_personalizadas_nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)
criando_actions_personalizadas_nfe_nao_emitida.short_description = "Action Personalizada - Nfe Não Emitida"