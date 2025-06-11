from django.contrib import admin

# Register your models here.

from .models import Estudiante, Ciudad
admin.site.register(Ciudad)
admin.site.register(Estudiante)
