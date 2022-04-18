from rest_framework import serializers
from .models import *

class ChefFiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefFiliere
        fields = '__all__'
class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'
class NoteSerializer(serializers.ModelSerializer):
    matiere_libele = serializers.CharField(source='matiere.libele')
    class Meta:
        model = Note
        fields = ('id', 'date', 'etudiant','matiere_libele','note')