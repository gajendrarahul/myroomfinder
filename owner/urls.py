from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.ownerpage, name='ownerpage'),
    path('addroom/', views.addroom, name='addroom'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)