from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import CategorySerializer, ProduitSerializer
from django.db import IntegrityError

from .forms import UserRegistrationForm, UserCreationForm
from .forms import ProduitForm
from .forms import CommandeForm
from .forms import FournisseurForm

from .models import Produit
from .models import Categorie
from .models import Commande
from .models import Fournisseur

# Create your views here.
def index(request):
    if( request.method == "POST" ):
        form = ProduitForm(request.POST,request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()
    products = Produit.objects.all()
    #context = {'products':products}
    #return render(request,'magasin/majProduits.html',{'form':form})
    return render(request, 'magasin/vitrine.html', {'list':products})#context est une variable python qui assure la communication avec le template
@login_required
def test(request):
    categories = Categorie.objects.all()
    context = {'categories':categories}
    return render(request,'magasin/test.html',context)

def commande(request):
    if( request.method == "POST" ):
        form = CommandeForm(request.POST, request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = CommandeForm()
    commandes = Commande.objects.all()
    
    return render(request, 'magasin/commande.html', {'form':form, 'commandes':commandes})
from django.db import IntegrityError

def nouvelleCommande(request):
    if request.method == "POST":
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else:
        form = CommandeForm()

    commandes = Commande.objects.all()
    context = {'form': form, 'commandes': commandes}
    return render(request, 'magasin/commande.html', context)

def nouveauFournisseur(request):
    if( request.method == "POST" ):
        form = FournisseurForm(request.POST, request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = FournisseurForm()
    listFour = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'form':form, 'fournisseurs':listFour})

def ajouterProduit(request):
    if( request.method == "POST" ):
        form = ProduitForm(request.POST,request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()
    
    return render(request,'magasin/majProduits.html',{'form':form})

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f'Coucou {username}, votre compte a été creé avec succès!')# not showing
            return redirect('acceuil')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    
    def get_queryset(self):
        queryset = Produit.objects.all()
        catId = self.request.GET.get('category_id')
        lib = self.request.GET.get('lib')
        if catId:
            queryset=queryset.filter(catégorie_id=catId)
        if lib:
            queryset= queryset.filter(libelle__contains= lib)
        return queryset
    
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        queryset = Categorie.objects.all()
        cat = self.request.GET.get('cat')
        if cat:
            queryset= queryset.filter(name__contains=cat)
        return queryset