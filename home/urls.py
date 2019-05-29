from django.urls import path
from .views import home, my_logout

# Estas views são baseadas em FBV - Functions based views
# Neste Curso vamos trabalhar com CBV - Class based views
from django.views.generic.base import TemplateView
from .views import HomePageView
from .views import MyView

urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name="logout"),

    #Class based views
    # ---- Se quisermos retornar um html simples ----
    path('home2/', TemplateView.as_view(template_name='home2.html')),

    # ---- Se quisermos injetar conteúdo ----
    path('home3/', HomePageView.as_view(template_name='home3.html')),

    # ---- Exemplo de View Simples ----
    path('view-simples/', MyView.as_view())
]