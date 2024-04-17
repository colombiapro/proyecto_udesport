from django import forms 
from .models import Eventos, Usuario, Deporte

class EventoForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = '__all__'
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        model2 = Deporte   
        fields = ('nombre',"programa","semestre")     