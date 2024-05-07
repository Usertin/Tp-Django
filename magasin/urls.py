from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin, auth
from .views import *

#from crispy_form import 

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('commande/', views.nouvelleCommande, name='commande'),
    path('ajouterProduit/', views.ajouterProduit, name='ajoutProduit'),
    path('nouveauFournisseur/', views.nouveauFournisseur, name='nouvFour'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name ='logout'),
    path('register/',views.register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produit', ProduitAPIView.as_view())
]