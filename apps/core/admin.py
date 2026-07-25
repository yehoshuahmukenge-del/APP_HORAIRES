from django.contrib import admin

from .models import (Chrono_Horaire, Cours, Disponibilite, Etudiant, Filiere,
                     Fonction, Personnel, Promotion, Role, Utilisateur, Utilisateur_Role)

admin.site.register((Utilisateur, Personnel, Etudiant, Role, Utilisateur_Role,
                     Filiere, Promotion, Cours, Fonction, Chrono_Horaire, Disponibilite))
