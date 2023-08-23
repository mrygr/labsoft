from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index),
    path('nosotros/', views.nosotros),
    path('productos/<id>', views.ver_camiseta),
    path('adminCamiseta/', views.adm_camiseta),
    path('crearCamiseta/', views.crear_camiseta),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
