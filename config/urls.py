"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *
from app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name = 'index'),
    path('areas/', area, name = 'areas'),
    path('fisicos/', fisico, name = 'fisicos'),
    path('invencoes/', invencao, name = 'invencoes'),
    path('subareas/', subarea, name = 'subareas'),
    path('pessoas/', pessoa, name = 'pessoa'),

    path("topicos/", TopicoListView.as_view(), name = 'topicoList'),
    path("topicos/<int:pk>/", TopicoDetailView.as_view(), name = 'topicoDetail'),

    path("questionarios/", QuestionarioListView.as_view(), name = 'questionarioList'),
    path("questionarios/<int:pk>/", QuestionarioDetailView.as_view(), name = 'questionarioDetail'),

    path("feedback/<int:questionario_id>/", views.submeter_respostas, name = 'submeter_respostas'),

    path('envios/', respondido, name = 'respondidos'),

]