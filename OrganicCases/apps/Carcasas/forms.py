from django import forms
from .models import Carcasa


class FormularioModificarCarcasa(forms.ModelForm):

    class Meta:
        model = Carcasa
        # Solo necesitamos estos atributos:
        fields = ['nombre', 'descripcion']
        # Y cambiar este widget para que la interfaz se vea mejor
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5,
                                                 'cols': 20,
                                                 }), }
