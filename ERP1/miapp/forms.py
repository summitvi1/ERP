from django import forms
from django.core import validators

class FormularioArticulo(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Mete el titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'EL titulo es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators= [
            validators.MaxLengthValidator(200, 'Te has pasado, has puesto mucho texto')
        ]
    )
    public = forms.TypedChoiceField(
        label = "Publicado?",
        choices = [(1, 'Si'),(0, 'No')]
    )