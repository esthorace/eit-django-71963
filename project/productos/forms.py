from django import forms

from .models import ProductoCategoria


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria
        # fields = ['nombre', 'decripcion']
        fields = '__all__'

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get('nombre', '')

        # Validar que sólo contenga letraas
        if not nombre.isalpha():
            raise forms.ValidationError('El nombre sólo puede contener letras')

        # Validar longitud de nombre
        if len(nombre) > 50 or len(nombre) < 3:
            raise forms.ValidationError(
                'El nombre debe tener una longitud mínima de 3 letras  o máxima de 50'
            )
        return nombre
