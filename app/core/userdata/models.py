from django.db import models
from django.db import models
from .genero import Generos
#Create your models here.
#Modelo de la tabla Roles:
class Roles(models.Model):
    roleName = models.CharField(max_length=50,verbose_name="Nombre del rol")
    class Meta:
        verbose_name ="Perfil de usuario"
        verbose_name_plural ="perfiles"

    #Creacion de la funcion para llamar atributos:        
    def __str__(self):
        return self.roleName
#Creacion de los modelos para la aplicacion datos user:
#Modelo de la tabla DatosUser:        
class DatosUser(models.Model):
    userDNI = models.CharField(max_length=20,verbose_name="ID de el usuario")
    nombreUser = models.CharField(max_length=255,verbose_name="Nombre")
    profecionUser = models.CharField(max_length=255, verbose_name="Profecion")
    fotoUser = models.ImageField(default='user.png', verbose_name="Foto de perfil", upload_to="perfiles/img")
    telUser = models.CharField(max_length=20)
    direccion=  models.CharField(max_length=255,verbose_name="Direccion de usuario")
    generoUser = models.CharField(max_length=10,choices=Generos,default="O",verbose_name="Genero")
    upData = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Creado")
    modificado = models.DateTimeField(auto_now=True,verbose_name="Modificado")
    
    class Meta:
        verbose_name ="Dato de usuario"
        verbose_name_plural ="Datos de los usuarios"
    
    def __str__(self):
        return self.nombreUser

#Modelo de la tabla Habilidades:         
class Habilidades(models.Model):
    nombreHabilidad = models.CharField(max_length=255,verbose_name="Nombre de la habilidad")
    descipcionHabilidad = models.TextField(max_length=2000,default="Desarrollador",verbose_name="Descripcion de habilidad")
   
    class Meta:
        verbose_name ="Habilidades del usuario"
        verbose_name_plural="Habilidades de los usuarios"
    #Funcion de seleccion:    
    def __str__(self):
        return self.nombreHabilidad

#Agregamos los modelos de detalle:         
class Rates(models.Model):
    idHabilidades = models.ForeignKey(Habilidades,on_delete=models.CASCADE,verbose_name="Id de la habilidad")
    idUSuario = models.ForeignKey(DatosUser,on_delete=models.CASCADE,verbose_name="Id del usuario")
    Porcentaje = models.DecimalField(max_digits=2,decimal_places=1,verbose_name="Porcentaje de dominio de la habilidad")
    udtHabilidad=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de actualizacion de la habilidad")
    
    class Meta:
        verbose_name ="Nivel de habilidad"
        verbose_name_plural ="Niveles de los usuarios"
    #Funcion para evocar:
    def __unicode__(self):
        return self.idUSuario
        
#Modelo de la tabla Detalles de roles:
class DetaRoles(models.Model):
    idRoles = models.ForeignKey(Roles, on_delete=models.CASCADE,verbose_name="Id del rol")
    idUsuario = models.ForeignKey(DatosUser,on_delete=models.CASCADE,verbose_name="Id del usuario")
    Agregado = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Fecha de agregacion del rol")
    addUser = models.DateTimeField(auto_now=True,verbose_name="Fecha de agregacion de user")
    EstadoRol = models.CharField(max_length=20,verbose_name="Estado del rol")
    
    class Meta:
        verbose_name ="Rol usuario"
        verbose_name_plural ="Roles de los usuarios"
    #Funcion de mostrar:
    def __unicode__(self):
        return self.idRoles
