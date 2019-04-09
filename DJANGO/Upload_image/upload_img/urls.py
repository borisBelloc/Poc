from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *



app_name = 'upload_img'

urlpatterns = [ 
    # path('', Login.as_view(), name="login"),
    # path('accueil', Accueil.as_view(), name="accueil"),

    path('', ImageCreateView.as_view(), name="image_create"),
    path('image/<int:pk>', ImageUpdateView.as_view(), name="image_update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)