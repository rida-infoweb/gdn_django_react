from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class ChefFiliereViewSet(viewsets.ModelViewSet):
    serializer_class = ChefFiliereSerializer
    queryset = ChefFiliere.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):

        if ChefFiliere.objects.filter(user=self.request.user):
            return self.queryset.filter(user=self.request.user)
        elif Enseignant.objects.filter(user=self.request.user):
            return self.queryset.filter(enseignant__user=self.request.user)
        elif Etudiant.objects.filter(user=self.request.user):
            return self.queryset.filter(etudiant__user=self.request.user)

class EnseignantViewSet(viewsets.ModelViewSet):
    serializer_class = EnseignantSerializer
    queryset = Enseignant.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if ChefFiliere.objects.filter(user=self.request.user):
             return self.queryset.filter(responsable__user=self.request.user)
        elif Enseignant.objects.filter(user=self.request.user):
             return self.queryset.filter(user=self.request.user)
        elif Etudiant.objects.filter(user=self.request.user):
            chefsFilieres=ChefFiliere.objects.filter(etudiant__user=self.request.user).values_list('user')
            return self.queryset.filter(responsable__user__in=chefsFilieres)


class EtudiantViewSet(viewsets.ModelViewSet):
    serializer_class = EtudiantSerializer

    queryset = Etudiant.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        
        if ChefFiliere.objects.filter(user=self.request.user):
            return self.queryset.filter(responsable__user=self.request.user)
        elif Enseignant.objects.filter(user=self.request.user):
            chefsFilieres=ChefFiliere.objects.filter(enseignant__user=self.request.user).values_list('user')
            return self.queryset.filter(responsable__user__in=chefsFilieres)
        elif Etudiant.objects.filter(user=self.request.user):
            return self.queryset.filter(user=self.request.user)
        


class MatiereViewSet(viewsets.ModelViewSet):
    serializer_class = MatiereSerializer
    queryset = Matiere.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        if ChefFiliere.objects.filter(user=self.request.user):
            return self.queryset.filter(instructeur__responsable__user=self.request.user)
        elif Enseignant.objects.filter(user=self.request.user):
            return self.queryset.filter(instructeur__user=self.request.user)
        elif Etudiant.objects.filter(user=self.request.user):
            chefsFilieres=ChefFiliere.objects.filter(etudiant__user=self.request.user).values_list('user')
            return self.queryset.filter(instructeur__responsable__user__in=chefsFilieres)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        if ChefFiliere.objects.filter(user=self.request.user):
            return self.queryset.filter(etudiant__responsable__user=self.request.user)
        elif Enseignant.objects.filter(user=self.request.user):
           return self.queryset.filter(matiere__instructeur__user=self.request.user)
        elif Etudiant.objects.filter(user=self.request.user):
            return self.queryset.filter(etudiant__user=self.request.user)
