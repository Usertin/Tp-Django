from django.db import models
from django.db.models import F
from datetime import date
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
    
class Categorie(models.Model):
    type_choices = [('Al','Alimentaire'), ('Mb','Meuble'), ('Sn','Sanitaire'), ('Vs','Vaisselle'), ('Vt','Vêtement'), ('Jx','Jouets'), ('Lg','Linge de Maison'), ('Bj','Bijoux'), ('Dc','Décor'), ('Im','Immobilier'), ('Pp','ParaPharmacie'), ('Em','Electromenager'), ('Tp','Tapis'), ('Fr','Frais')]
    name = models.CharField(max_length=50, choices = type_choices, default='Al')

    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField(default='test adresse')
    email = models.EmailField(default='test email')
    telephone = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.email+" "+self.telephone
    
class Produit(models.Model):
    type_choices = [('fr','frais'), ('cs','conserver'), ('em','emballé')]
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10,decimal_places=3)
    type = models.CharField(max_length=2, choices=type_choices, default='em')
    img = models.ImageField(blank=True)
    catégorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.libelle+' '+self.description+' '+str(self.prix)+' '+self.type
    
class ProduitNC(Produit):
    duree_guarantie = models.CharField(max_length=100)
    
    def __str__(self):
        return super().__str__() +" "+self.duree_guarantie 

class Commande(models.Model):
    dateCde = models.DateField(null = True, default = date.today)
    produits = models.ManyToManyField('Produit')
    totalCde = models.FloatField(editable=False, default=0.0)
    
    def recalculTotal(self):
        totalCde = sum(produit.prix for produit in self.produits.all())
    
    def __str__(self):
        affichage = str(self.dateCde)+" "+str(self.totalCde)
        for produit in self.produits.all():
            affichage += ' '+produit.libelle+' '+str(produit.prix)+'DT' +' '+produit.description+'/'
        
        return affichage
    
@receiver(m2m_changed, sender=Commande.produits.through) 
def update_total(sender, instance, **kwargs): 
    if kwargs['action'] in ['post_add', 'post_remove', 'post_clear']: 
        instance.recalculTotal()