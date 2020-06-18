from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
    	return render(request, self.template_name, {})

#Vista basada en función
def contacto(request):
	formContact = ContactForm()
    #Validar que el formulario tenga una petición post
	if request.method == "POST":
		#Reconfiguramos formContact con los datos que hemos enviado, es decir rellenamos la plantilla del formulario
		formContact = ContactForm(data=request.POST)
		if formContact.is_valid():
			tipomsj = request.POST.get('tipomsj','')
			usuario = request.POST.get('usuario','')
			correo = request.POST.get('correo','')
			mensaje = request.POST.get('mensaje','')

			#Creamos el objetocon las variables del formulario
			email = EmailMessage(
				"RepoDevelopers: Tienes un nuevo mensaje de contacto",
				"De {} <{}>\n\nEscribió:\n\n{}".format(usuario, correo, mensaje),
				"no-contestar@inbox.mailtrap.io",
				["dayhanavelez01@gmail.com"],
				reply_to=[correo]
				)
			#Enviar correo
			try:
				email.send()
                #Se envia correo
				return redirect(reverse('contacto')+"?ok")
			except:
				#No se ha enviado el correo
				return redirect(reverse('contacto')+"?fail")

	return render(request, 'contacto.html', {'formulario':formContact})