import csv
from datetime import date
import io
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.db.models import Count

#borrrar #
from .forms import BusquedaForm
from .models import mantenimiento
#hasta aqui #



class loginView(View):

    def get(self, request):
        form = loginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = loginForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            clave = form.cleaned_data["clave"]
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect("personal")
            else:
                return self.get(request)


class genericocrearlistarview(View):
    campos = []
    model = None
    form = None
    TITULO_TABLA = None
    editarview = None
    eliminarview = None
    puedoeditar = True
    puedoeliminar = True
  
    def condicionlistar(self,request): 
        return True

    def render(self, request, form):
        puedolistar = self.condicionlistar(request)
        objetos=[]
        if puedolistar:
            instaciasdb = self.model.objects.all()
            # selecciona todas las insatnacias de la base de dato
            instaciasdb = self.model.objects.all()
            # recorre cada instancia y extae los datos para usar en la tabla
            # recorre la instancia de la base de datos

            for instaciadb in instaciasdb:
                objeto = []
                for campo in self.campos:
                    # pk referencia a id
                    valor = instaciadb.__dict__.get(campo)
                    if not valor or valor == 'None':
                        valor = ""
                    objeto.append(valor)
                # ordena la tabla
                objetos.append({"objeto": objeto, "editar": self.editarview +
                                  str(instaciadb.pk), "eliminar": self.eliminarview+str(instaciadb.pk)})
        
            return render(request, 'genericocrearlistar.html', {'genericoForm': form, 'objetos': sorted(objetos, key=lambda objeto: objeto["objeto"][0]), 'campos': self.campos, 'TITULO_TABLA': self.TITULO_TABLA,"puedolistar":puedolistar, "puedoeditar": self.puedoeditar, "puedoeliminar": self.puedoeliminar})

        return render(request, 'genericocrearlistar.html', {'genericoForm': form, 'objetos':[], 'campos': self.campos, 'TITULO_TABLA': self.TITULO_TABLA , "puedolistar":puedolistar, "puedoeditar": self.puedoeditar, "puedoeliminar": self.puedoeliminar})

    # crear lista
    def get(self, request):
        # crear nueva instancia
        form = self.form()
        return self.render(request, form)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            form = self.form()
        return self.render(request, form)


class genericoeditarview(UpdateView):
    template_name = "editar.html"

class genericoeliminar(DeleteView):
    template_name = "eliminar.html"

class personalView(genericocrearlistarview):
    telefono = models.CharField(max_length=15, null=True, blank=True)
    campos = ['id', 'cedula','nombres', 'apellidos', 'fecha_nacimiento', 'ciudad_nacimiento',
              'telefono', 'telefono', 'idtiposangre', 'idrango', 'idsubCircuito','vehiculo_asignado']
    model = personaModel
    form = personaForm
    TITULO_TABLA = 'PERSONAL POLICIAL'
    editarview = "/personal/editar/"
    eliminarview = "/personal/eliminar/"
#editar-eliminar persona# 
class editarpersonaview(genericoeditarview):
    model = personaModel
    fields = ['nombres', 'apellidos']
    success_url = reverse_lazy("personal")

class eliminarpersonaview(genericoeliminar):
    model = personaModel
    success_url = reverse_lazy("personal")

#vehiculo #
class vehiculoView(genericocrearlistarview):
    campos = ['id', 'placa', 'chasis', 'marca', 'placa', 'motor', 'kilometraje', 'cilindraje',
              'capacidad_carga', 'capacidad_pasajeros', 'idsubCircuito', 'idtipoVehiculo', 'idtipoCombustible']
    model = vehiculoModel
    form = vehiculoForm
    TITULO_TABLA = "Flota Vehicular"
    editarview = "/vehiculo/editar/"
    eliminarview = "/vehiculo/eliminar/"

# editar y eliminar vehiculo

class editarvehiculoview(genericoeditarview):
    model = vehiculoModel
    fields = ['placa', 'chasis']
    success_url = reverse_lazy("vehiculo")

class eliminarvehiculoview(genericoeliminar):
    model = vehiculoModel
    success_url = reverse_lazy("vehiculo")
    
#dependencia-provincia#
class dependenciaView(genericocrearlistarview):
    campos = ['id', 'nombre', 'provincia']
    model = dependencia
    form = dependenciaForm
    TITULO_TABLA = "dependencia"
    editarview = ""
    eliminarview = ""
    
#circuito#
class circuitoView(genericocrearlistarview):
    campos = ['id', 'nombreCircuito', 'nombreParroquia', 'iddependencia_id']
    model = circuito
    form = circuitoForm
    TITULO_TABLA = "circuito"
    editarview = ""
    eliminarview = ""

#subcircuito#
class subCircuitoView(genericocrearlistarview):
    campos = ['id', 'nombreSubCircuito', 'idCircuito_id']
    model = subCircuito
    form = subCircuitoForm
    TITULO_TABLA = "Sub Circuito"
    editarview = ""
    eliminarview = ""


#MAntenimiento#

class mantenimientoView(genericocrearlistarview):
    campos = ['fecha', 'descripcion','idvehiculo','idtipomantenimiento']
    model = mantenimiento
    form = mantenimientoForm
    TITULO_TABLA = "Matenimiento"
    editarview = ""
    eliminarview = ""

#busqueda mantenimeitn#
def buscar_mantenimientos(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            mantenimientos = mantenimiento.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
            context = {'form': form, 'mantenimientos': mantenimientos}
            return render(request, 'buscar_mantenimientos.html', context)
    else:
        form = BusquedaForm()
    context = {'form': form}
    return render(request, 'buscar_mantenimientos.html', context)

def descargar_mantenimientos(request, fecha_inicio, fecha_fin):
    mantenimientos = mantenimiento.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mantenimientos.csv"'
    writer = csv.writer(response)
    writer.writerow(['Fecha', 'Descripción', 'Vehículo', 'Tipo de mantenimiento'])
    for m in mantenimientos:
        writer.writerow([m.fecha, m.descripcion, m.idvehiculo, m.idtipomantenimiento])
    return response
#busqeuda persona #

def buscar_persona(request):
    resultados = []
    if request.method == 'GET' and 'cedula' in request.GET:
        cedula = request.GET.get('cedula')
        resultados = personaModel.objects.filter(cedula=cedula).select_related('idsubCircuito')
    return render(request, 'buscar_persona.html', {'resultados': resultados})

def descargar_resultados(request):
    cedula = request.GET.get('cedula')
    personas = personaModel.objects.filter(cedula=cedula).select_related('idsubCircuito')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Persona.csv"'

    # Escribir encabezados
    response.write('Cedula,Nombres,Apellidos,Telefono,Subcircuito\n')

    # Escribir datos
    for persona in personas:
        subcircuito = persona.idsubCircuito.nombreSubCircuito if persona.idsubCircuito else ""
        response.write(f'{persona.cedula},{persona.nombres},{persona.apellidos},{persona.telefono},{subcircuito}\n')

    return response

#buscar vehiculo#

def buscar_vehiculo(request):
    resultados = []
    if request.method == 'GET' and 'placa' in request.GET:
        placa = request.GET.get('placa')
        try:
            vehiculo = vehiculoModel.objects.get(placa=placa)
            resultados.append({
                'placa': vehiculo.placa,
                'marca': vehiculo.marca,
                'subcircuito': vehiculo.idsubCircuito.nombreSubCircuito
            })
        except vehiculoModel.DoesNotExist:
            pass  # No se encontró ningún vehículo con la placa especificada
    return render(request, 'buscar_vehiculo.html', {'resultados': resultados})

def descargar_resultados_vehiculo(request):
    placa = request.GET.get('placa')
    vehiculo = vehiculoModel.objects.get(placa=placa)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="resultados_vehiculo.csv"'

    # Escribir encabezados
    response.write('Placa,Marca,Subcircuito\n')

    # Escribir datos
    response.write(f'{vehiculo.placa},{vehiculo.marca},{vehiculo.idsubCircuito.nombreSubCircuito}\n')

    return response

#ejemplop#


def solicitud_movilizacion(request):
    if request.method == 'POST':
        form = SolicitudMovilizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitud_movilizacion')
    else:
        form = SolicitudMovilizacionForm()
    
    datos = Movilizacion.objects.all()
    return render(request, 'solicitud.html', {'form': form, 'datos': datos})

def registrar_combustible(request):
    if request.method == 'POST':
        form = RegistroCombustibleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_combustible')
    else:
        form = RegistroCombustibleForm()
    
    registros_combustible = RegistroCombustible.objects.all()
    return render(request, 'combustible.html', {'form': form, 'registros_combustible': registros_combustible})

##vcista de la pistola ##

def pistola_view(request):
    if request.method == 'POST':
        form = PistolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pistola')
    else:
        form = PistolaForm()
    pistolas = Pistola.objects.all()
    return render(request, 'pistola.html', {'form': form, 'pistolas': pistolas})

