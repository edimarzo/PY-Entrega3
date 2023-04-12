from django import forms


class AltaAgenteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    legajo = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    
    
class BuscarAgente(forms.Form):
    apellido = forms.CharField(max_length=20, required=False)