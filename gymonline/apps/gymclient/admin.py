from django.contrib import admin
from gymonline.apps.gymclient import models

# Register your models here.
class ClaseAdminModel(admin.ModelAdmin):
    class Meta:
        models.Clase
    
admin.site.register(models.Clase, ClaseAdminModel)