from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
#Importar modelos de otras app:
from userdata.models import DatosUser
# Create your models here.
#Modelo de la tabla Tipo de documento:
class TipoDocu(models.Model):
	nombTiDoc= models.CharField(max_length=45,verbose_name="Nombre del Tipo de documento")

	class Meta:
		verbose_name="Tipo documento"
		verbose_name_plural="Tipos de documento"
    #Creacion de la funcion para llamar atributos:
	def __str__(self):
	   return self.nombTiDoc 

#Modelo de la tabla categoria de proyecto:
class CategProye(models.Model):
	lenguaje = models.CharField(max_length=45,verbose_name="Lenguaje")
	motorDB= models.CharField(max_length=155,verbose_name="Motor de la base de datos")
	arquitectura= models.CharField(max_length=155,verbose_name="Arquitectura")

	class Meta:
		verbose_name="Categoria de proyecto"
		verbose_name_plural="Categorias de proyectos"
	
	def __str__(self):
		return self.lenguaje

#Modelo de la tabla Proyectos:
class Proyectos(models.Model):
	idCategProye = models.ForeignKey(CategProye, on_delete=models.CASCADE,verbose_name="Id de la categoria de proyecto")
	nombProye = models.CharField(max_length=255,verbose_name="Nombre del proyecto")
	descProy = models.TextField(max_length=2000,verbose_name="Descripcion del proyecto")
	imgProye = models.ImageField(default='proye.png',verbose_name="Imagen del proyecto")
	FechaIni = models.DateTimeField(auto_now_add=False,verbose_name="Fecha de inicio del proyecto")
	FechaFin = models.DateTimeField(auto_now_add=False,verbose_name="Fecha del final del proyecto")
	urlRepo = models.TextField(max_length=2000,verbose_name="Direccion del repositorio")
	EstaProy = models.CharField(max_length=45,verbose_name="Estado del Proyecto")

	class Meta:
		verbose_name="Proyecto"
		verbose_name_plural="Proyectos"

	def __str__(self):
		return self.nombProye

#Modelo de la tabla Documentos:
class Documentos(models.Model):
	idTipoDocu = models.ForeignKey(TipoDocu, on_delete=models.CASCADE,verbose_name="Id del tipo de documento")
	idProyectos = models.ForeignKey(Proyectos, on_delete=models.CASCADE,verbose_name="Id del proyecto")
	idUsuarios = models.ForeignKey(DatosUser, on_delete=models.CASCADE,verbose_name="Id del usuario")
	nombDocu = models.CharField(max_length=30,verbose_name="Nombre del documento")
	pathDocu = models.TextField(max_length=2000,verbose_name="Direccion del git")

	class Meta:
		verbose_name="Documento"
		verbose_name_plural="Documentos"
	
	def __unicode__(self):
		return self.idTipoDocu
	


		

