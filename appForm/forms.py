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
    diasSemana = forms.MultipleChoiceField(label='Dias de la semana', required=False,widget=forms.CheckboxSelectMultiple, choices=DIAS_SEMANA)
    email = forms.EmailField(label='Email', required=True, help_text='Formato del email: xxx@iesmartinezm.es')

    def clean(self): #Cuando quiero comparar dos campos, es cuando se usa def clean(self).
        # Como queremos comparar fechaInicio y Fecha Fin, va aquí
        cleaned_data = super().clean()
        fechaInicio = cleaned_data.get('fechaInicio')
        fechaFin = cleaned_data.get('fechaFin')


        if fechaInicio and fechaFin: #Sirve para verificar que tienen valores y no son NONE
                                     #con AND vemos que ambas son verdaderas
            if fechaFin < fechaInicio:
                raise forms.ValidationError("Error: No puede ser la fecha final anterior a la inicial. Debe ser igual o superior a la fecha inicial.")


    def clean_diasSemana(self):

        dia_semana_data = self.cleaned_data['diasSemana']
        if not dia_semana_data: #Indicamos que no puede ser NONETYPE
            raise forms.ValidationError("Error: No se ha seleccionado ningún valor")

        if len(dia_semana_data)>3:
                raise forms.ValidationError("Error: No puedes seleccionar más de 3 días")

        return dia_semana_data

    def clean_email(self):

        email_data = self.cleaned_data['email']
        if '@iesmartinezm.es' not in email_data:
            raise forms.ValidationError('Error: El email debe ser de dominio @iesmartinezm.es')
        return email_data

      #  email = cleaned_data.get('email')
      #  if email and not email.endswith('@iesmartinezm.es'): #Si es el campo email no es NONE y además, no termina en @iesmartinezm.es
       #     raise forms.ValidationError("El email debe ser de dominio @iesmartinezm.es")

