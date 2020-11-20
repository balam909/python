from django.contrib import admin
from principal.models import Actor, Pelicula

# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	pass

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
	pass
