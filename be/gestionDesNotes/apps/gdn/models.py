
from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

User = get_user_model()

class ChefFiliere(models.Model): 
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    codeChefFiliere = models.CharField(max_length=200, verbose_name="Code Chef de filière",unique=True, error_messages={'unique':"Code Chef de filière déjà existant !"})
    def __str__(self):
        return f"{self.user}" 
    class Meta:
        db_table = 'ChefFiliere'
        db_table = 'Chef de filière'
        verbose_name_plural = 'Chefs de filières'

class Enseignant(models.Model): 
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    responsable = models.ForeignKey(ChefFiliere, on_delete=models.PROTECT,verbose_name="Chef de filière")
    codeEnseignant = models.CharField(max_length=200, verbose_name="Code Enseignant",unique=True, error_messages={'unique':"Code Enseignant déjà existant !"})
    def __str__(self):
        return f"{self.user}" 
    class Meta:
        db_table = 'Enseignant'
        db_table = 'Enseignant'
        verbose_name_plural = 'Enseignants'


class Etudiant(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    responsable = models.ForeignKey(ChefFiliere, on_delete=models.PROTECT,verbose_name="Responsable")
    numapogee = models.CharField(max_length=200, verbose_name="N° Apogée",unique=True, error_messages={'unique':"N° Apogée déjà existant !."})
    def __str__(self):
        return f"{self.user}" 
    class Meta:
        db_table = 'Etudiant'
        db_table = 'Étudiant'
        verbose_name_plural = 'Étudiants'     


class Matiere(models.Model):

    instructeur = models.ForeignKey(Enseignant, on_delete=models.PROTECT,verbose_name="Instructeur")
    libele = models.CharField(max_length=200, verbose_name="Matière",unique=True, error_messages={'unique':"Matière déjà existante !"})


    def __str__(self):
        return f"{self.libele}" 
    class Meta:
        db_table = 'Matiere'
        db_table = 'Matière'
        verbose_name_plural = 'Matières'  



class Note(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT,verbose_name="Matière")
    date = models.DateField( default=datetime.date.today, verbose_name="Date d\'examen")
    etudiant = models.ForeignKey(Etudiant, on_delete=models.PROTECT,verbose_name="Étudiant")
    note=models.DecimalField(validators=[MinValueValidator(0),MaxValueValidator(20)],verbose_name="Note", max_digits=4, decimal_places=2, )
    class Meta:
        db_table = 'Note'
        db_table = 'Note'
        verbose_name_plural = 'Notes'  

    def __str__(self):
        return f"{self.etudiant.numapogee} - {self.date} - {self.note}/20" 