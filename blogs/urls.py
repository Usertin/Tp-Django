from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib import admin, auth
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import ListePosts, DetailPost, CreerPost, SupprimerPost, ModifierPost

urlpatterns = [
    path('', ListePosts.as_view(), name='liste_posts'),
    path('<int:pk>', DetailPost.as_view(), name='detail_post'),
    path('ajouter/', CreerPost.as_view(), name="creer_post"),
    path('<int:pk>/supprimer/', SupprimerPost.as_view(), name="supprimer_post"),
    path('<int:pk>/modifier/', ModifierPost.as_view(), name="modifier_post"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
