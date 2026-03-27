# traer las propiedades de dorms.py#
from django import forms
from .models import *

class FormularioProductos(forms.ModelForm):
    class Meta:
        model=Productos
        fields='__all__'
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

        
