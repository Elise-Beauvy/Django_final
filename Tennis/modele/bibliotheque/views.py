"""from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import JoueurForm
from .models import JoueurModel"""
from django.shortcuts import render, redirect
from .forms import JoueurForm
from .forms import PaysForm
from . import models
from .models import JoueurModel
from .models import Pays
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = JoueurForm(request)
        if form.is_valid():
            joueur = form.save()
            return HttpResponseRedirect("/bibliotheque/")
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = JoueurForm()
        return render(request,"bibliotheque/ajout.html",{"form" : form})

def traitement(request):
    lform = JoueurForm(request.POST)
    if lform.is_valid():
        joueur = lform.save(commit=False)
        joueur.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})


def index(request):
    liste = JoueurModel.objects.all()
    return render(request, 'bibliotheque/index.html', {'liste': liste})

def affiche(request, id):
    joueur = JoueurModel.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"joueur" : joueur})

def delete(request, id):
    joueur = JoueurModel.objects.get(pk=id)
    joueur.delete()
    return HttpResponseRedirect("/bibliotheque/")

def update(request, id):
    joueur = JoueurModel.objects.get(pk=id)
    lform = JoueurForm(joueur.dico())
    return render(request, "bibliotheque/update.html", {"form": lform,"id":id})

def traitementupdate(request, id):
    lform = JoueurForm(request.POST)
    if lform.is_valid():
        joueur = lform.save(commit=False)
        joueur.id = id;
        joueur.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})

def ajout_nationalite(request):
    submitted = False
    if request.method == 'POST':
        form = PaysForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/bibliotheque/liste_nationalite/")
    else:
        form = PaysForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'Etat/ajout_nationalite.html', {'form':form, 'submitted':submitted})

def liste_nationalite(request):
   liste = JoueurModel.objects.all()
   liste_nationalite = Pays.objects.all()
   return render(request, 'Etat/liste_nationalite.html', {'liste_nationalite': liste_nationalite,"liste":liste})

def update_nationalite(request, id):
    nationalite = Pays.objects.get(pk=id)
    form = PaysForm(request.POST or None, instance=nationalite)
    if form.is_valid():
        form.save()
        return redirect("Pays")
    return render(request, 'Etat/update_nationalite.html', {'nationalite':nationalite, 'form':form})

def delete_nationalite(request, id):
    nationalite = Pays.objects.get(pk=id)
    nationalite.delete()
    return HttpResponseRedirect("/bibliotheque/liste_nationalite/")
