from django import forms

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
    fechaInicio = forms.DateField(label='Fecha inicial', required=True, input_formats=['%d/%m/%Y'],
                                  help_text="Formato de la fecha: dd/MM/yyyy")
    fechaFin = forms.DateField(label='Fecha final', required=True, input_formats=['%d/%m/%Y'],
                               help_text="Formato de la fecha: dd/MM/yyyy")
    diasSemana = forms.MultipleChoiceField(label='Dias de la semana', required=True,
                                           widget=forms.CheckboxSelectMultiple, choices=DIAS_SEMANA)
    email = forms.EmailField(label='Email', required=True, help_text='Formato del email: xxx@iesmartinezm.es')

    def clean(self):
        cleaned_data = super().clean()
        fechaInicio = self.cleaned_data['fechaInicio']
        fechaFin = self.cleaned_data['fechaFin']
        diasSemana = self.cleaned_data['diasSemana']
        email = self.cleaned_data['email']

        if fechaFin < fechaInicio:  # si es 3 de noviembre el inicio, la final tiene q ser 4 o más
            raise forms.ValidationError(
                "Error: No puede ser la fecha final anterior a la inicial. Debe ser igual o superior a la fecha inicial.")

        if len(diasSemana) >= 1 or len(diasSemana) > 3:
            raise forms.ValidationError('No se puede señalar más de tres días de la semana.')

        if not email.endswith('@iesmartinezm.es'):
            raise forms.ValidationError('El formato del email debe ser xxx@martinezm.es')
