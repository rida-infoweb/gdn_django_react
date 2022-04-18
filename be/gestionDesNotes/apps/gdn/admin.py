from django.contrib import admin
from .models import *

class ChefFiliereAdmin(admin.ModelAdmin):
    list = ('user','codeChefFiliere','codeEnseignant', 'cin', 'nom','prenom','created_at','updated_at')

    admin.site.register(ChefFiliere)

class EnseignantAdmin(admin.ModelAdmin):
    list = ('user','responsable','codeEnseignant', 'cin', 'nom','prenom','created_at','updated_at')

    admin.site.register(Enseignant)

class EtudiantAdmin(admin.ModelAdmin):
    list = ('user','responsable','numapogee', 'cin', 'nom','prenom','created_at','updated_at')

    admin.site.register(Etudiant)

class MatiereAdmin(admin.ModelAdmin):
    list = ('instructeur','libele','created_at','updated_at')

    admin.site.register(Matiere)

class NoteAdmin(admin.ModelAdmin):
    list = ('matiere','date','etudiant','note','created_at','updated_at')

    admin.site.register(Note)

