from django.contrib import admin
from bloc.models import Finance
# Register your models here.
class AdminFinance(admin.ModelAdmin):
    list_display = ('name', 'price', 'description','slug','actif')

    # Autres configurations éventuelles pour l'administration des finances
    # ...

# Enregistrement du modèle Finance avec la classe d'administration personnalisée
admin.site.register(Finance, AdminFinance)

