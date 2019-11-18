from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.listar_grado, name ='listar_grado'),
    url(r'^grado/nuevo/$', views.grado_nuevo, name='grado_nuevo'),
    ]