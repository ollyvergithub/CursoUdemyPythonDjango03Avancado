from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Estas views são baseadas em FBV - Functions based views
# Neste Curso vamos trabalhar com CBV - Class based views
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View

def home(request):
    #import pdb; pdb.set_trace()
    print("Estou aqui")
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return redirect('home')


# Estas views são baseadas em FBV - Functions based views
# Neste Curso vamos trabalhar com CBV - Class based views
class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Olá seja bem vindo ao curso de Django advanced'
        return context


class MyView(View):
    # Criar uma função para cada verbo Http
    def get(self, request, *args, **kwargs):
        #return HttpResponse('Hello, World!')

        #Podemos retornar um template também
        return render(request, 'view-simples.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'view-simples-post.html')


