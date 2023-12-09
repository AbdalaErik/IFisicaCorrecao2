from django import forms
from .models import *

from django.forms import Textarea

class SubareaForm(forms.ModelForm):

    class Meta:

        model = Subarea

        fields = '__all__'

        widgets = {
            "descricao": Textarea(attrs={"cols": 100, "rows": 4}),
        }

class TopicoForm(forms.ModelForm):

    class Meta:

        model = Topico

        fields = '__all__'

        widgets = {
            "descricao": Textarea(attrs={"cols": 100, "rows": 8}),
        }

class QuestaoForm(forms.ModelForm):

    class Meta:

        model = Questao

        fields = '__all__'

        widgets = {
            "enunciado": Textarea(attrs={"cols": 100, "rows": 6}),
            "alternativa_a": Textarea(attrs={"cols": 100, "rows": 4}),
            "alternativa_b": Textarea(attrs={"cols": 100, "rows": 4}),
            "alternativa_c": Textarea(attrs={"cols": 100, "rows": 4}),
            "alternativa_d": Textarea(attrs={"cols": 100, "rows": 4}),
            "alternativa_e": Textarea(attrs={"cols": 100, "rows": 4}),
        }

class FisicoForm(forms.ModelForm):

    class Meta:

        model = Fisico

        fields = '__all__'

        widgets = {
            "biografia": Textarea(attrs={"cols": 100, "rows": 4}),
        }

class AreaForm(forms.ModelForm):

    class Meta:

        model = Area

        fields = '__all__'

        widgets = {
            "descricao": Textarea(attrs={"cols": 100, "rows": 4}),
        }

class QuestionarioForm(forms.ModelForm):

    class Meta:

        model = Questionario

        fields = '__all__'

        widgets = {
            "descricao": Textarea(attrs={"cols": 100, "rows": 4}),
        }