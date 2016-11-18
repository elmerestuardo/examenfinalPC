from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^prestamos$', views.ingreso_prestamo),
]
