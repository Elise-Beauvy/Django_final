from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class PaysForm(ModelForm):
    class Meta:
        model=models.Pays
        fields=('nationalite',)
        labels = {
            'nationalite': _('Nom Pays'),
        }

class JoueurForm(ModelForm):
    class Meta:
        model = models.JoueurModel
        fields = ('Nom', 'Prenom', 'Naissance', 'date_debut_circuit','Nationalite')
        labels = {
            'Nom' : _('Nom'),
            'Prenom' : _('Prenom') ,
            'Naissance' : _('Naissance'),
            'date_debut_circuit' : _('date de début sur le circuit'),
            'Nationalite' : _('Nationalite'),
        }

