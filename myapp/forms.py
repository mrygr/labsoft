from django import forms
from .models import Camiseta

class Camiseta_form(forms.ModelForm):
    class Meta: 
        model = Camiseta
        fields = {"nombre", "descripcion", "precio", "imagen"}