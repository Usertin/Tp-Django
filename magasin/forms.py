from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Produit
from .models import Commande
from .models import Fournisseur
#from crispy_forms.helper import FormHelper

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"
        #fields = ['libelle','description']
        
class CommandeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        #self.fields['author'].disabled = False
        
        self.fields['dateCde'].widget.attrs['class'] = 'form-control'
        self.fields['produits'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Commande
        fields = "__all__"
    
class FournisseurForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        #self.fields['author'].disabled = False
        
        self.fields['nom'].widget.attrs['class'] = 'form-control'
        self.fields['adresse'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['telephone'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Fournisseur
        fields = "__all__"

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Prénom")
    last_name = forms.CharField(label="Nom")
    email = forms.EmailField(label="Adress e-mail")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields+('first_name','last_name','email')