from django.db import models
from django import forms
from django.core.exceptions import ValidationError

# Create your models here.
class QuienesSomos(models.Model):
    primerBloqueTexto = models.CharField(max_length=2000)
    SegundoBloqueTexto = models.CharField(max_length=1500)
    imagenprimerBloqueTexto=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenSegundoBloqueTexto=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen5=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen6=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen7=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen8=models.ImageField(upload_to="Imagenes",null=True,blank=True)


    class Meta:
        verbose_name="QuienesSomos"
        verbose_name_plural="QuienesSomoss"

class QuienesSomosForm(forms.ModelForm):
    primerBloqueTexto = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
    SegundoBloqueTexto= forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
    class Meta:
        model = QuienesSomos
        fields = '__all__'
    
class SabiasQ(models.Model):
    nombreDelArticulo = models.CharField(max_length=100)
    descripcionDelArticulo = models.CharField(max_length=100)
    leerMas= models.CharField(max_length=1000)
    imagen1=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    class Meta:
        verbose_name="SabiasQs"
        verbose_name_plural="SabiasQs"


class Excursion1(models.Model):
    def save(self, *args, **kwargs):
            if not self.pk and Excursion1.objects.exists():
                raise ValidationError("No se permite crear más excursiones")
            return super().save(*args, **kwargs)

    nombreDeLaExcursion = models.CharField(max_length=1000,null=True)
    descripcionDeLaExcursion = models.CharField(max_length=1000,null=True)
    duracion = models.CharField(max_length=1000)
    servicioQueIncluye = models.CharField(max_length=1000)
    minimoDePersonas = models.CharField(max_length=1000)
    puntoDePartida = models.CharField(max_length=1000)
    Informacion = models.CharField(max_length=10000)
    alerta = models.CharField(max_length=1000)
    imagenCarrusel1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel5=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    imagen1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen5=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen6=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen7=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen8=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    
    def __str__(self):
        return self.nombreDeLaExcursion

class Excursion1Form(forms.ModelForm):
    Informacion = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
    descripcionDeLaExcursion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    minimoDePersonas = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    servicioQueIncluye = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    puntoDePartida = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    alerta = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))

    class Meta:
        verbose_name="Excursion1s"
        verbose_name_plural="Excursion1ss"
    



class Excursion2(models.Model):
    def save(self, *args, **kwargs):
        if not self.pk and Excursion2.objects.exists():
            raise ValidationError("No se permite crear más excursiones")
        return super().save(*args, **kwargs)

    # Agregar el resto de los campos de acuerdo a tus necesidades
    nombreDeLaExcursion = models.CharField(max_length=1000, null=True)
    descripcionDeLaExcursion = models.CharField(max_length=1000, null=True)
    duracion = models.CharField(max_length=1000)
    servicioQueIncluye = models.CharField(max_length=1000)
    minimoDePersonas = models.CharField(max_length=1000)
    puntoDePartida = models.CharField(max_length=1000)
    Informacion = models.CharField(max_length=2000)
    alerta = models.CharField(max_length=1000)
    imagenCarrusel1 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagenCarrusel2 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagenCarrusel3 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagenCarrusel4 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagenCarrusel5 = models.ImageField(upload_to="Imagenes", null=True, blank=True)

    imagen1 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen2 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen3 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen4 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen5 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen6 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen7 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen8 = models.ImageField(upload_to="Imagenes", null=True, blank=True)

    def __str__(self):
        return self.nombreDeLaExcursion

class Excursion2Form(forms.ModelForm):
    Informacion = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
    descripcionDeLaExcursion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    minimoDePersonas = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    servicioQueIncluye = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    puntoDePartida = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    alerta = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))

    class Meta:
        verbose_name="Excursion2s"
        verbose_name_plural="Excursion2ss"

class Excursion3(models.Model):

    def save(self, *args, **kwargs):
            if not self.pk and Excursion3.objects.exists():
                raise ValidationError("No se permite crear más excursiones")
            return super().save(*args, **kwargs)
    
    nombreDeLaExcursion = models.CharField(max_length=1000,null=True)
    descripcionDeLaExcursion = models.CharField(max_length=1000,null=True)
    duracion = models.CharField(max_length=1000)
    servicioQueIncluye = models.CharField(max_length=1000)
    minimoDePersonas = models.CharField(max_length=1000)
    puntoDePartida = models.CharField(max_length=1000)
    Informacion = models.CharField(max_length=10000)
    alerta = models.CharField(max_length=1000)
    imagenCarrusel1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel5=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    imagen1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen5=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen6=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen7=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen8=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    class Meta:
        verbose_name="Excursion3s"
        verbose_name_plural="Excursion3ss"

class Excursion3Form(forms.ModelForm):
    Informacion = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
    descripcionDeLaExcursion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    minimoDePersonas = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    servicioQueIncluye = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    puntoDePartida = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    alerta = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))

class Excursion4(models.Model):
    def save(self, *args, **kwargs):
            if not self.pk and Excursion3.objects.exists():
                raise ValidationError("No se permite crear más excursiones")
            return super().save(*args, **kwargs)

    nombreDeLaExcursion = models.CharField(max_length=1000,null=True)
    descripcionDeLaExcursion = models.CharField(max_length=1000,null=True)
    duracion = models.CharField(max_length=1000)
    servicioQueIncluye = models.CharField(max_length=1000)
    minimoDePersonas = models.CharField(max_length=1000)
    puntoDePartida = models.CharField(max_length=1000)
    Informacion = models.CharField(max_length=10000)
    alerta = models.CharField(max_length=1000)
    imagenCarrusel1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel5=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    imagen1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen5=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen6=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen7=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen8=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    class Meta:
        verbose_name="Excursion4s"
        verbose_name_plural="Excursion4ss"
class Excursion4Form(forms.ModelForm):
    Informacion = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
    descripcionDeLaExcursion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    minimoDePersonas = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    servicioQueIncluye = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    puntoDePartida = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    alerta = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))


class Excursion5(models.Model):

    def save(self, *args, **kwargs):
            if not self.pk and Excursion3.objects.exists():
                raise ValidationError("No se permite crear más excursiones")
            return super().save(*args, **kwargs)

    nombreDeLaExcursion = models.CharField(max_length=1000,null=True)
    descripcionDeLaExcursion = models.CharField(max_length=1000,null=True)
    duracion = models.CharField(max_length=1000)
    servicioQueIncluye = models.CharField(max_length=1000)
    minimoDePersonas = models.CharField(max_length=1000)
    puntoDePartida = models.CharField(max_length=1000)
    Informacion = models.CharField(max_length=10000)
    alerta = models.CharField(max_length=1000)
    imagenCarrusel1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel5=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    imagen1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen5=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen6=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen7=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen8=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    class Meta:
        verbose_name="Excursion5s"
        verbose_name_plural="Excursion5ss"
class Excursion5Form(forms.ModelForm):
    Informacion = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
    descripcionDeLaExcursion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    minimoDePersonas = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    servicioQueIncluye = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    puntoDePartida = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
    alerta = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))

class Excursion6(models.Model):
    def save(self, *args, **kwargs):
            if not self.pk and Excursion3.objects.exists():
                raise ValidationError("No se permite crear más excursiones")
            return super().save(*args, **kwargs)

    nombreDeLaExcursion = models.CharField(max_length=1000,null=True)
    descripcionDeLaExcursion = models.CharField(max_length=1000,null=True)
    duracion = models.CharField(max_length=1000)
    servicioQueIncluye = models.CharField(max_length=1000)
    minimoDePersonas = models.CharField(max_length=1000)
    puntoDePartida = models.CharField(max_length=1000)
    Informacion = models.CharField(max_length=10000)
    alerta = models.CharField(max_length=1000)
    imagenCarrusel1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagenCarrusel5=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    imagen1=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen2=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen3=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen4=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen5=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen6=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen7=models.ImageField(upload_to="Imagenes",null=True,blank=True)
    imagen8=models.ImageField(upload_to="Imagenes",null=True,blank=True)

    class Meta:
        verbose_name="Excursion6s"
        verbose_name_plural="Excursion6ss"
class Excursion6Form(forms.ModelForm):
   Informacion = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 120}))
   descripcionDeLaExcursion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
   minimoDePersonas = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
   servicioQueIncluye = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
   puntoDePartida = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))
   alerta = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 120}))

class Provincia(models.Model):
    
    HABANA = 'Habana'
    PINAR_DEL_RIO = 'Pinar del Rio'
    MATANZAS = 'Matanzas'
    CIENFUEGOS = 'Cienfuegos'
    ARTEMISA = 'Artemisa'
    MAYABEQUE='Mayabeque'
    VILLA_CLARA = 'Villa Clara'
    LAS_TUNAS= 'Las Tunas'
    GRANMA='Granma'
    HOLGUIN= 'Holguin'
    GUANTANAMO = 'Guantánamo'
    SANTIAGO_DE_CUBA = 'Santiago de Cuba'
    SACTI_SPIRITUS = 'Sancti Spíritus'
    CIEGO_DE_AVILA= 'Ciego de Ávila'
    ISLA_DE_LA_JUVENTUD ='Isla de la Juventud'


    PROVINCIA_CHOICES = [
        (HABANA, 'Habana'),
        (PINAR_DEL_RIO, 'Pinar del Rio'),
        (MATANZAS, 'Matanzas'),
        (CIENFUEGOS, 'Cienfuegos'),
        (ARTEMISA, 'Artemisa'),
        (MAYABEQUE, 'Mayabeque'),
        (VILLA_CLARA, 'Villa Clara'),
        (LAS_TUNAS, 'Las Tunas'),
        (GRANMA, 'Granma'),
        (HOLGUIN, 'Holguin'),
        (GUANTANAMO, 'Guantánamo'),
        (SANTIAGO_DE_CUBA, 'Santiago de Cuba'),
        (SACTI_SPIRITUS, 'Sancti Spíritus'),
        (CIEGO_DE_AVILA, 'Ciego de Ávila'),
        (ISLA_DE_LA_JUVENTUD, 'Isla de la Juventud'),
    ]

    provincia = models.CharField(max_length=50, choices=PROVINCIA_CHOICES, null=True)

    def __str__(self):
                return self.provincia
    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"

    
        



class Casas(models.Model):    
    municipioLocacion = models.CharField(max_length=50, null=True)
    nombreCasa = models.CharField(max_length=50, null=True)
    Informacion = models.CharField(max_length=1000)
    provincias=models.ManyToManyField(Provincia,related_name='producto_subcat')
    imagenPrincipal = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    
    imagen2 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen3 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen4 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen5 = models.ImageField(upload_to="Imagenes", null=True, blank=True)
    imagen6 = models.ImageField(upload_to="Imagenes", null=True, blank=True)

    def __str__(self):
            return self.nombreCasa

    class Meta:
        verbose_name = "Casas"
        verbose_name_plural = "Casass"

