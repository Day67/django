from django import forms
from .pqrsf import pqrsf

#Creamos las clases con los formularios pertinentes
class ContactForm(forms.Form):
	#Atributos del formulario de contacto
	tipomsj = forms.ChoiceField(label= "Tipo de mensaje", required=True, choices=pqrsf, widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Tipo de mensaje'}))
	usuario = forms.CharField(label= "Nombre", required=True, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Nombre'}))
	correo = forms.EmailField(label= "Email", required=True, widget=forms.EmailInput(attrs={'class':'input', 'placeholder':'Email'}))
	mensaje = forms.CharField(label= "Mensaje", required=True, widget=forms.Textarea(attrs={'class':'input', 'placeholder':'Mensaje', 'cols':'30', 'rows':'10'}))