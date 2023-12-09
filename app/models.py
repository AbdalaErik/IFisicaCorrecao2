from django.db import models

# Create your models here.

class Area(models.Model):

    nome = models.CharField(max_length = 80, verbose_name="Nome")
    descricao = models.CharField(max_length = 300, verbose_name="Descrição")

    class Meta:

        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):

        return f'{self.nome}'
    
class Subarea(models.Model):

    nome = models.CharField(max_length = 80, verbose_name="Nome")
    descricao = models.CharField(max_length = 300, verbose_name="Descrição")
    area = models.ForeignKey(Area, on_delete = models.CASCADE, verbose_name="Área")

    class Meta:

        verbose_name = "Subárea"
        verbose_name_plural = "Subáreas"

    def __str__(self):

        return f'{self.area} - {self.nome}'
    
class Topico(models.Model):

    nome = models.CharField(max_length = 80, verbose_name="Nome")
    descricao = models.CharField(max_length = 2000, verbose_name="Descrição")
    subarea = models.ForeignKey(Subarea, on_delete = models.CASCADE, verbose_name="Subárea")

    class Meta:

        verbose_name = "Tópico"
        verbose_name_plural = "Tópicos"

    def __str__(self):

        return f'[{self.subarea}] - {self.nome}'
    
class Questionario(models.Model):

    titulo = models.CharField(max_length = 80, verbose_name="Título")
    descricao = models.CharField(max_length = 300, verbose_name="Descrição")
    area = models.ForeignKey(Area, on_delete = models.CASCADE, verbose_name="Área")

    class Meta:

        verbose_name = "Questionário"
        verbose_name_plural = "Questionários"

    def __str__(self):

        return f'[{self.area}] - {self.titulo}'
    
class Questao(models.Model):

    questionario = models.ForeignKey(Questionario, on_delete = models.CASCADE, verbose_name="Questionário")
    titulo = models.CharField(max_length = 80, verbose_name="Título")
    enunciado = models.CharField(max_length = 500, verbose_name="Enunciado")
    alternativa_a = models.CharField(max_length = 300, verbose_name="Alternativa A")
    alternativa_b = models.CharField(max_length = 300, verbose_name="Alternativa B")
    alternativa_c = models.CharField(max_length = 300, verbose_name="Alternativa C")
    alternativa_d = models.CharField(max_length = 300, verbose_name="Alternativa D")
    alternativa_e = models.CharField(max_length = 300, verbose_name="Alternativa E")
    alternativa_correta = models.CharField(max_length = 1, verbose_name="Alternativa correta")

    class Meta:

        verbose_name = "Questão"
        verbose_name_plural = "Questões"

    def __str__(self):

        return f'{self.titulo}'
    
class Ocupacao(models.Model):

    nome = models.CharField(max_length = 30, verbose_name="Nome")

    class Meta:

        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

    def __str__(self):

        return f'{self.nome}'
    
class Pessoa(models.Model):

    nome = models.CharField(max_length = 80, verbose_name="Nome")
    ocupacao = models.ForeignKey(Ocupacao, on_delete = models.CASCADE, verbose_name="Ocupação")

    class Meta:

        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):

        return f'[{self.ocupacao}] - {self.nome}'
    
class Integrante(Pessoa):

    email = models.CharField(max_length = 50, verbose_name="Email")

    class Meta:

        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"

    def __str__(self):

        return f'[{self.ocupacao}] - {self.nome}'
    
class Fisico(Pessoa):

    biografia = models.CharField(max_length = 300, verbose_name="Biografia")
    data_nascimento = models.DateField(verbose_name="Data de nascimento")

    class Meta:

        verbose_name = "Físico"
        verbose_name_plural = "Físicos"

    def __str__(self):

        return f'{self.nome}'
    
class Invencao(models.Model):

    nome = models.CharField(max_length = 80, verbose_name="Nome")
    ano = models.DateField(verbose_name="Ano")
    fisico = models.ManyToManyField(Fisico, verbose_name="Físico")
    area = models.ManyToManyField(Area, verbose_name="Área")

    class Meta:

        verbose_name = "Invenção"
        verbose_name_plural = "Invenções"

    def __str__(self):

        return f'{self.nome}'
    
class QuestionarioRespondido(models.Model):

    questionario = models.ForeignKey(Questionario, on_delete = models.CASCADE, verbose_name="Questionário")
    integrante = models.ForeignKey(Integrante, on_delete = models.CASCADE, verbose_name="Integrante")
    data_realizacao = models.DateTimeField(verbose_name="Data de realização")
    numero_acertos = models.PositiveIntegerField(verbose_name="Número de acertos")
    respostas_integrante = models.TextField(blank = True, null = True, verbose_name="Respostas do integrante")

    class Meta:

        verbose_name = "Questionário respondido"
        verbose_name_plural = "Questionários respondidos"

    def __str__(self):

        return f'{self.questionario} {self.integrante}'