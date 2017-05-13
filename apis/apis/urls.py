from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns
from gestion.views import *

from django.conf.urls import url
from django.contrib import admin


urlpatterns = [


    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', 'jwt_auth.views.obtain_jwt_token'),
    url(r'^llamadas/(\w+)$', 'gestion.views.llamadas'),
    url(r'^contactos$', 'gestion.views.contactos'),
    url(r'^acciones/(\w+)$', 'gestion.views.acciones'),
    url(r'^estados/(\w+)$', 'gestion.views.estados'),
    url(r'^todosestados$', 'gestion.views.todosestados'),
    url(r'^tipifica$', 'gestion.views.tipifica'),
    url(r'^base/(\w+)$', 'gestion.views.base'),
    url(r'^cliente/(\w+)$', 'gestion.views.cliente'),
    url(r'^listaacciones$', 'gestion.views.listaacciones'),
    url(r'^reporte/$', 'gestion.views.reporte'),
    url(r'^llamadasxdni/(\w+)$', 'gestion.views.llamadasxdni'),
    url(r'^saveagente/(\w+)/(\w+)$', 'gestion.views.saveagente'),
    url(r'^traebase/(\w+)$', 'gestion.views.traebase'),
    url(r'^trama/(\w+)$', 'gestion.views.trama'),
    url(r'^generatrama$', 'gestion.views.generatrama'),
    url(r'^actualizabbva$', 'gestion.views.actualizabbva'),
    url(r'^venta$', 'gestion.views.venta'),
    url(r'^reportebbva/(\w+)$', 'gestion.views.reportebbva'),
    url(r'^audios/$', 'gestion.views.audios'),
    url(r'^ventas$', 'gestion.views.ventas'),
    url(r'^reportebbva/(\w+)$', 'gestion.views.reportebbva'),
    url(r'^audios/$', 'gestion.views.audios'),
    url(r'^actualizatrama$', 'gestion.views.actualizatrama'),
    url(r'^ventarecupero$', 'gestion.views.ventarecupero'),
    url(r'^preguntas$', 'gestion.views.preguntas'),
    url(r'^ticket/(\w+)$', 'gestion.views.ticket'),
    url(r'^noactualiza/(\w+)$', 'gestion.views.noactualiza'),
    url(r'^agentes$', 'gestion.views.agentes'),
    url(r'^distrito$', 'gestion.views.distrito'),
    url(r'^distrito$', 'gestion.views.distrito'),
    url(r'^provincia/(\w+)$', 'gestion.views.provincia'),
    url(r'^departamentos/$', 'gestion.views.departamentos'),
    url(r'^distrito/(\w+)$', 'gestion.views.distrito'),
    url(r'^tramaweb$', 'gestion.views.tramaweb'),
    url(r'^uploadfile$', 'gestion.views.uploadfile'),
    url(r'^gentrama/(\w+)$', 'gestion.views.gentrama'),
    url(r'^actaudio$', 'gestion.views.actaudio'),
    url(r'^arreglachubb$', 'gestion.views.arreglachubb'),
    url(r'^reporteticket$', 'gestion.views.reporteticket'),
    url(r'^reporteticketlineal$', 'gestion.views.reporteticketlineal'),
    url(r'^actualizaticket$', 'gestion.views.actualizaticket'),
    url(r'^generaticketactualiza/(\w+)$', 'gestion.views.generaticketactualiza'),
    url(r'^generaticketventa/(\w+)$', 'gestion.views.generaticketventa'),
    url(r'^generaticketventa/(\w+)$', 'gestion.views.generaticketventa'),
    url(r'^generaencriptado$', 'gestion.views.generaencriptado'),


    #Hotels



]