from django import forms
from .models import tarea
class tareaform(forms.ModelForm):
    class meta:
        model=tarea
        fields=['tarea']
        