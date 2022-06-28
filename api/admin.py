from django.contrib import admin
from .models import Mega_sena_concurso, Mega_sena_valores

@admin.register(Mega_sena_concurso)
class Mega_sena_concursoAdmin(admin.ModelAdmin):
    list_display = (Mega_sena_concurso, "data")

@admin.register(Mega_sena_valores)
class Mega_sena_valoresoAdmin(admin.ModelAdmin):
    list_display = (Mega_sena_valores, "v1", "v2", "v3", "v4", "v5", "v6")