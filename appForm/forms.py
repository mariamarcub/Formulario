from django import forms
import re


DIAS_SEMANA = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo'),
]


class CreaFormularioForm(forms.Form):
    fechaInicio = forms.DateField(label='Fecha inicial', required=True, input_formats=['%d/%m/%Y'],help_text="Formato de la fecha: dd/MM/yyyy")
    fechaFin = forms.DateField(label='Fecha final', required=True, input_formats=['%d/%m/%Y'],help_text="Formato de la fecha: dd/MM/yyyy")
    diasSemana = forms.MultipleChoiceField(label='Dias de la semana', required=True,widget=forms.CheckboxSelectMultiple, choices=DIAS_SEMANA)
    email = forms.EmailField(label='Email', required=True, help_text='Formato del email: xxx@iesmartinezm.es')

    def clean(self):
        cleaned_data = super().clean()
        fechaInicio = cleaned_data.get('fechaInicio')
        fechaFin = cleaned_data.get('fechaFin')
        diasSemana = cleaned_data.get('diasSemana')
        email = cleaned_data.get('email')

        if fechaInicio and fechaFin: #Sirve para verificar que tienen valores y no son NONE
                                     #con AND vemos que ambas son verdaderas
            if fechaFin < fechaInicio:
                raise forms.ValidationError("Error: No puede ser la fecha final anterior a la inicial. Debe ser igual o superior a la fecha inicial.")

        if diasSemana: #Indicamos que no es NONE, que tiene un valor
            if len(diasSemana)<1 or len(diasSemana)>3:
                raise forms.ValidationError("Error: No puedes seleccionar menos de 1 días y más de 3 días")

        if email and not email.endswith('@iesmartinezm.es'): #Si es el campo email no es NONE y además, no termina en @iesmartinezm.es
            raise forms.ValidationError("El email debe ser de dominio @iesmartinezm.es")

