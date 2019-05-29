from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from .models import Person
from .forms import PersonForm

# Estas views são baseadas em FBV - Functions based views
# Neste Curso vamos trabalhar com CBV - Class based views
from django.utils import timezone

# List Views
from django.views.generic.list import ListView

# Detail View
from django.views.generic.detail import DetailView

# Create View
from django.views.generic.edit import CreateView

# Update View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

# Delete View
from django.views.generic.edit import DeleteView

#Bulk Create
from django.views.generic import View
from .models import Produto

@login_required
def persons_list(request):
    persons = Person.objects.all()
    print("O Resultado Foi | ", persons)
    return render(request, 'person.html', {'persons' : persons})

@login_required
def persons_new(request):
    form =  PersonForm(request.POST or None,request.FILES or None)

    if(form.is_valid()):
        form.save()
        return redirect('persons_list')

    return render(request, 'person_form.html', {'form':form})

@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if(form.is_valid()):
        form.save()
        return redirect('persons_list')

    return render(request, 'person_form.html', {'form':form})

@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if (request.method == 'POST'):
        person.delete()
        return redirect('persons_list')

    return render(request, 'person_delete_confirm.html', {'form': form, 'person': person})

# Estas views são baseadas em FBV - Functions based views
# Neste Curso vamos trabalhar com CBV - Class based views
# List View
class PersonList(ListView):
    model = Person

# Detail View
class PersonDetailView(DetailView):
    model = Person
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# Create View
class PersonCreateView(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/listar-com-class-based-views'

# Update View
class PersonUpdateView(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listar-com-class-based-views')

# Delete View
class PersonDeleteView(DeleteView):
    model = Person
    #success_url = reverse_lazy('listar-com-class-based-views')

    # Entra no lugar do success_url
    def get_success_url(self):
        return reverse_lazy('listar-com-class-based-views')


#Bulk Create
class ProdutoBulk(View):
    def get(self, request):
        produtos = ['banana', 'maca', 'limao', 'laranja', 'pera', 'melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)


        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')




