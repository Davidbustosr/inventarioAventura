from django import forms

from experiencias.models import Categoria, Experiencia


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ExperienciaForm(forms.ModelForm):
    # El campo 'creador' NO va en el formulario: se asigna solo con request.user en la vista
    class Meta:
        model = Experiencia
        fields = ['titulo', 'descripcion', 'categoria', 'precio', 'cupo_maximo', 'fecha', 'activa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cupo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'},
                                         format='%Y-%m-%dT%H:%M'),
        }

    # Validaciones personalizadas: clean_<nombre del campo>
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 1000:
            raise forms.ValidationError('El precio mínimo es $1000.')
        return precio

    def clean_cupo_maximo(self):
        cupo = self.cleaned_data.get('cupo_maximo')
        if cupo < 1:
            raise forms.ValidationError('El cupo debe ser de al menos 1 persona.')
        return cupo
