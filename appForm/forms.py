from django import forms

class CreaFormularioForm(forms.Form):
    fechaInicio = forms.DateField(label='Fecha inicial', required= True)
    fechaFin = forms.DateField(label='Fecha final', required=True)
    diasSemana = forms.CharField(label='Dias de la semana', required=True)
    email = forms.EmailField(label='Email', required=True)