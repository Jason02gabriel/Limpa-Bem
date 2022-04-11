from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('cliente','telefone','endereco','bairro','cidade','estado','cep','Serviço','data_limpeza','obs')