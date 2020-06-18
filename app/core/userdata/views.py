from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from userdata.models import DatosUser

# Create your views here.
class NosotrosPageView(ListView):

	model = DatosUser
	template_name = "nosotros.html"

	