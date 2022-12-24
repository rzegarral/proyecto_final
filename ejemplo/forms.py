from django import forms
from ejemplo.models import Familiar, Amigos

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100,
  
  widget=forms.TextInput(attrs={'placeholder': 'Digite nombre o apellido'}))

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']
'''
class AmigosForm(forms.ModelForm):
  class Meta:
    model = Amigos
    fields = ['nombre', 'direccion', 'pais', 'Edad']
    '''    