from django.conf.urls import url, include 
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("ChefFiliere", ChefFiliereViewSet, basename='chefFiliere')
router.register("Enseignant", EnseignantViewSet, basename='enseignant')
router.register("Etudiant", EtudiantViewSet, basename='etudiant')
router.register("Matiere", MatiereViewSet, basename='matiere')
router.register("Note", NoteViewSet, basename='note')
gdn_urlpatterns = [url("api/", include(router.urls))]