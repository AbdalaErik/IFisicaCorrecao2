from typing import Any
from django.shortcuts import render, get_object_or_404
from . models import *

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import HttpResponseNotFound

from django.utils import timezone
from datetime import datetime

import json

# Create your views here.

def area(request):

    areas = {
        'areas':Area.objects.all()
    }

    return render(request, 'exibicao/area.html', areas)

def subarea(request):

    subareas = {
        'subareas':Subarea.objects.all(),
        'areas':Area.objects.all()
    }

    return render(request, 'exibicao/subarea.html', subareas)

def fisico(request):

    fisicos = {
        'fisicos':Fisico.objects.all()
    }

    return render(request, 'exibicao/fisico.html', fisicos)

def invencao(request):

    invencoes = {
        'invencoes':Invencao.objects.all()
    }

    return render(request, 'exibicao/invencao.html', invencoes)

def ocupacao(request):

    ocupacoes = {
        'ocupacoes':Ocupacao.objects.all()
    }

    return render(request, 'exibicao/ocupacao.html', ocupacoes)

def pessoa(request):

    pessoas = {
        'pessoas':Pessoa.objects.all(),
        'alunos':Integrante.objects.filter(ocupacao__nome = 'Aluno(a)').values(),
        'professores':Integrante.objects.filter(ocupacao__nome = 'Professor(a)').values(),
    }

    return render(request, 'exibicao/pessoa.html', pessoas)

def questionario(request):

    questionarios = {
        'questionarios':Questionario.objects.all()
    }

    return render(request, 'exibicao/questionario.html', questionarios)

class TopicoListView(ListView):
    
    model = Area

    context_object_name = "areas"

    template_name = "exibicao/topico/topico-list.html"

class TopicoDetailView(DetailView):

    model = Topico

    context_object_name = "topico"

    template_name = "exibicao/topico/topico-detail.html"

class QuestionarioListView(ListView):

    model = Questionario

    context_object_name = "questionarios"

    template_name = "exibicao/questionario/questionario-list.html"

class QuestionarioDetailView(DetailView):

    model = Questionario

    context_object_name = "questionario"

    template_name = "exibicao/questionario/questionario-detail.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        membros = Integrante.objects.all()

        context['membros'] = membros

        return context

def submeter_respostas(request, questionario_id):

    questionario = get_object_or_404(Questionario, pk = questionario_id)

    questoes = questionario.questao_set.all()

    if request.method == 'POST':

        integrante_id = request.POST.get('membro')

        integrante = get_object_or_404(Integrante, pk = integrante_id)

        numero_acertos = 0

        respostas = {}

        for questao in questoes:

            nome_input = f'Q{questao.id}'

            resposta = request.POST.get(nome_input)

            respostas[questao.id] = resposta

            if resposta == questao.alternativa_correta:

                numero_acertos += 1

        respostas_json = json.dumps(respostas)

        fuso_horario = timezone.get_current_timezone()

        data_e_hora = datetime.now()
        data_e_hora_com_timezone = timezone.make_aware(data_e_hora, fuso_horario)

        questionario_respondido = QuestionarioRespondido.objects.create(
            questionario = questionario,
            integrante = integrante,
            data_realizacao = data_e_hora_com_timezone,
            numero_acertos = numero_acertos,
            respostas_integrante = respostas_json
        )

        questionario_respondido.save()

        respostas_corretas = {}

        for questao in questoes:

            respostas_corretas[questao.id] = questao.alternativa_correta

        lista_respostas = zip(respostas, respostas.values(), respostas_corretas.values())
        
        context = {
            'lista_respostas': lista_respostas,
        }

        return render(request, 'exibicao/agradecimento.html', context)
    
    return HttpResponseNotFound('<h1>Página não encontrada</h1>')

def respondido(request):

    respondidos = {
        'respondidos':QuestionarioRespondido.objects.all()
    }

    return render(request, 'exibicao/respondido.html', respondidos)