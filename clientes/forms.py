from django.forms import ModelForm
from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'class': 'btn btn-primary'})
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'class': 'btn btn-primary'})

    class Meta:
        model = Person

        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo' ]
        labels= {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'age': 'Idade',
            'salary': 'Salário',
            'bio': 'Biografia',
            'photo': 'Imagem',
        }





