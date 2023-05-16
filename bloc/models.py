from django.db import models

# Create your models here.
#créer ma classe poir la base de données
class Finance(models.Model):
    name=models.CharField(max_length=150)
    price =models.DecimalField(max_digits=1000000,decimal_places=5)
    description=models.TextField()
    class Meta:
        verbose_name =("Finance")
        verbose_name_plural=("Finances")

    #surchargepour afficher le non dans la base de donnée

    def __str__(self):
         return self.name

    """chaque fois que je modifie ma table ou ma classe du modèle voici les deux commandes à insserer 
    Python manage.py makemigrations
    python manage.py migrate
    """