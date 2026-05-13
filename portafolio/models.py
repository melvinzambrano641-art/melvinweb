from django.db import models


class Portafolio(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='portafolio', null=True, blank=True, verbose_name="Imagen")
    link = models.URLField(null=True, blank=True, verbose_name="Enlace")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"
        ordering = ["-created"]
        db_table = "portfolio"

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombres")
    subtitle = models.CharField(max_length=200, verbose_name="Carrera")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='profile', verbose_name="Imagen")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")
    email = models.EmailField(null=True, blank=True, verbose_name="Correo")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        db_table = "profile"

    def __str__(self):
        return self.name