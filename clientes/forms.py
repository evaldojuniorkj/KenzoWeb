from django import forms
from .models import Pessoa


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'