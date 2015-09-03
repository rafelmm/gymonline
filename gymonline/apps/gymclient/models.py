from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils.timezone import utc
from gymonline.apps.gymclient import managers

# Create your models here.
class Clase(models.Model):
    INTENSIDAD_CHOICES = (
            ('A', _('Alta')),
            ('M', _('Media')),
            ('B', _('Baja')),
    )
    # Attributes
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=150,
                                   blank=True,
                                   help_text = _("Escribe una descripcion para la clase (opcional)"))
    intensidad = models.CharField(max_length=1, 
                                  choices=INTENSIDAD_CHOICES,
                                  default='M')
    fecha_alta = models.DateField(verbose_name=_("Fecha alta"))
    fecha_modificacion = models.DateField(verbose_name=_("Fecha modificacion"))
    fecha_baja = models.DateField(verbose_name=_("Fecha baja"))
    popularidad = models.IntegerField()
    
    #Manager
    objects = managers.gymclientManager()
    
    # Functions
    def __unicode__(self):
        return _("Clase %s") % self.nombre

    def save(self, *args, **kwargs):
        self.fecha_modificacion = datetime.datetime.utcnow().replace(tzinfo = utc)
        super(Clase, self).save(args, kwargs)

    # Meta
    class Meta:
        verbose_name = _("Clase")
        verbose_name_plural = _("Classes")
        ordering = ["-id"]
        