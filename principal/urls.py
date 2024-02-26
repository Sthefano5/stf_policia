from datetime import date
from django.urls import include, path, register_converter
from . import views
from .views import buscar_mantenimientos, descargar_mantenimientos
from .views import buscar_vehiculo, descargar_resultados_vehiculo


urlpatterns = [
    path('', views.loginView.as_view(), name='login'),
    path('login/', views.loginView.as_view(), name='login'),    
    path('personal/', views.personalView.as_view(), name='personal'),
    path('personal/editar/<int:pk>',views.editarpersonaview.as_view(), name='editarpersona'),
    path('personal/eliminar/<int:pk>',views.eliminarpersonaview.as_view(), name='eliminarpersona'),
   #vehiculos#
    path('vehiculo/', views.vehiculoView.as_view(), name='vehiculo'),
    path('vehiculo/editar/<int:pk>',views.editarvehiculoview.as_view(), name='editarvehiculo'),
    path('vehiculo/eliminar/<int:pk>',views.eliminarvehiculoview.as_view(), name='eliminarvehiculo'),
   #dependencia-provincia#
   path('dependencia/', views.dependenciaView.as_view(), name='dependencia'),
   #circuito#
   path('circuito/', views.circuitoView.as_view(), name='circuito'),
   #Subcircuito#
   path('subcircuito/', views.subCircuitoView.as_view(), name='subcircuito'),
   #Mantenimiento#
   path('mantenimiento/', views.mantenimientoView.as_view(), name='mantenimiento'),
   #borrar #
   path('buscarmantenimientos/', buscar_mantenimientos, name='buscar_mantenimientos'),
   path('descargar/<fecha_inicio>/<fecha_fin>/', descargar_mantenimientos, name='descargar_mantenimientos'),
   #persona buscar #
   path('buscar_personal/', views.buscar_persona, name='buscar_persona'),
   path('descargar/', views.descargar_resultados, name='descargar_resultados'),
  #buscar vehiculo #
  path('buscar_vehiculo/', buscar_vehiculo, name='buscar_vehiculo'),
  path('descargar/', descargar_resultados_vehiculo, name='descargar_resultados_vehiculo'),
  
  #ejemplo#
    ##path('solicitud/', views.solicitud, name='solicitud'),
   ##path('solicitud/', views.solicitud_movilizacion, name='solicitud'),
   path('solicitud/', views.solicitud_movilizacion, name='solicitud_movilizacion'),
   path('registrar_combustible/', views.registrar_combustible, name='registrar_combustible'),
   
   path('pistola/',views.pistola_view, name='pistola'),
   path('perchero/',views.perchero_view, name='perchero'),









   
 ]
