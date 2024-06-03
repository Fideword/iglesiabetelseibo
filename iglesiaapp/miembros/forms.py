from django import forms
from .models import Miembro, Servicio, Actividade, Socie, Minist, Esc_Dom

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        exclude = []

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        exclude = []

class ActividadeForm(forms.ModelForm):
    class Meta:
        model = Actividade
        exclude = []

class SocieForm(forms.ModelForm):
    class Meta:
        model = Socie
        exclude = []

class MinistForm(forms.ModelForm):
    class Meta:
        model = Minist
        exclude = []

class Esc_DomForm(forms.ModelForm):
    class Meta:
        model = Esc_Dom
        exclude = []

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

