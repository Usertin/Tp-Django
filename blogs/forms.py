from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #*args : tuple pour les parametres dont on recupere par index. example : args[0]
    #**kwargs: dictionnaire pour les parametres dont on recupaere par cle. example : kwargs['user']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        #self.fields['author'].disabled = False
        
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['slug'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        
        if user:
            user_choice = (user.id, str(user))
            self.fields['author'].initial = user_choice
        
    class Meta:
        model = Post
        fields = ['title','slug','image','status','content','author']
