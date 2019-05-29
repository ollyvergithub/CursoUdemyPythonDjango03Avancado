from django.contrib import admin
from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete

# Estas views são baseadas em FBV - Functions based views
# Neste Curso vamos trabalhar com CBV - Class based views

# List View
from .views import PersonList

# Destail View
from .views import PersonDetailView

# Create View
from .views import PersonCreateView

# Update View
from .views import PersonUpdateView

# Update View
from .views import PersonDeleteView

#Bulk Create
from .views import ProdutoBulk

urlpatterns = [
    path('list/', persons_list, name='persons_list'),
    path('new/', persons_new, name='persons_new'),
    path('update/<int:id>', persons_update, name='persons_update'),
    path('delete/<int:id>', persons_delete, name='persons_delete'),

    # Estas views são baseadas em FBV - Functions based views
    # Neste Curso vamos trabalhar com CBV - Class based views
    # List View
    path('listar-com-class-based-views/', PersonList.as_view(), name='listar-com-class-based-views'),

    # Destail View
    path('detailview-com-class-based-views/<int:pk>/', PersonDetailView.as_view(), name='detailview-com-class-based-views'),

    # Create View
    path('create-com-class-based-views/', PersonCreateView.as_view(), name='create-com-class-based-views'),

    # Update View
    path('update-com-class-based-views/<int:pk>/', PersonUpdateView.as_view(), name='update-com-class-based-views'),

    # Update View
    path('delete-com-class-based-views/<int:pk>/', PersonDeleteView.as_view(), name='delete-com-class-based-views'),

    #Bulk Create
    path('person_bulk', ProdutoBulk.as_view(), name='person-bulk'),

 ]
