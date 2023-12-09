from django.contrib import admin
from app.models import *
from app.forms import *

# Register your models here.

# admin.site.register(Area)
# admin.site.register(Subarea)
# admin.site.register(Topico)
# admin.site.register(Fisico)
admin.site.register(Invencao)
# admin.site.register(Questao)
# admin.site.register(Questionario)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(QuestionarioRespondido)
admin.site.register(Integrante)

# Inline para Area e Subarea:

class SubareaInline(admin.TabularInline):

    model = Subarea

    form = SubareaForm

    extra = 1

class AreaAdmin(admin.ModelAdmin):

    inlines = [SubareaInline]

    form = AreaForm

# Inline para Subarea e Topico:

class TopicoInline(admin.TabularInline):

    model = Topico

    form = TopicoForm

    extra = 1

class SubareaAdmin(admin.ModelAdmin):

    inlines = [TopicoInline]

    form = SubareaForm
    
admin.site.register(Area, AreaAdmin)
admin.site.register(Subarea, SubareaAdmin)

# Inline Questionario e Questao:

class QuestaoInline(admin.TabularInline):

    model = Questao

    form = QuestaoForm

    extra = 1

    exclude = ('enunciado', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'alternativa_e',)

class QuestionarioAdmin(admin.ModelAdmin):

    inlines = [QuestaoInline]

    form = QuestionarioForm
    
admin.site.register(Questionario, QuestionarioAdmin)

# Adaptando as caixas de texto da seção Administrativa:

class FisicoAdmin(admin.ModelAdmin):

    form = FisicoForm

admin.site.register(Fisico, FisicoAdmin)

class TopicoAdmin(admin.ModelAdmin):

    form = TopicoForm

admin.site.register(Topico, TopicoAdmin)

class QuestaoAdmin(admin.ModelAdmin):

    form = QuestaoForm

admin.site.register(Questao, QuestaoAdmin)