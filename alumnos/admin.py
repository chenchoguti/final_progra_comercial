from django.contrib import admin
from .models import Materia, MateriaAdmin, Grado, GradoAdmin, Seccion
# Register your models here.


admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Seccion)
