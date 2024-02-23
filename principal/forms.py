from datetime import date
from django import forms
from .models import personaModel  # Asumiendo que tienes un modelo llamado Persona
# Asumiendo que tienes un modelo llamado Persona
from .models import *

class loginForm(forms.Form):
    usuario = forms.CharField()
    clave = forms.CharField(widget=forms.PasswordInput())


class personaForm(forms.ModelForm):
    class Meta:
        model = personaModel
        # Lista de campos que quieres incluir en el formulario
        fields = ['cedula', 'nombres', 'apellidos', 'fecha_nacimiento', 'ciudad_nacimiento', 'telefono', 'telefono',
                  'idtiposangre', 'idrango', 'idsubCircuito', 'vehiculo_asignado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha_nacimiento"].widget = forms.SelectDateWidget()

#formulario de vehiculos #
 
class vehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculoModel
        fields = ['placa', 'chasis', 'marca', 'placa', 'motor', 'kilometraje', 'cilindraje','capacidad_carga', 'capacidad_pasajeros', 'idsubCircuito', 'idtipoVehiculo', 'idtipoCombustible']

#dependencia-provincia#
class dependenciaForm(forms.ModelForm):
    class Meta:
        model = dependencia
        fields = ['nombre', 'provincia']
#circuito#
class circuitoForm(forms.ModelForm):
    class Meta:
        model = circuito
        fields = ['nombreCircuito', 'nombreParroquia', 'iddependencia']

#subcircuito#
class subCircuitoForm(forms.ModelForm):
    class Meta:
        model = subCircuito
        fields = ['nombreSubCircuito', 'idCircuito']
        
#matenimiento#
class mantenimientoForm(forms.ModelForm):
    class Meta:
        model = mantenimiento
        fields = ['fecha', 'descripcion','idvehiculo','idtipomantenimiento']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha"].widget = forms.SelectDateWidget()
        
#borrar en caso de de salir mal #
class BusquedaForm(forms.Form):
    fecha_inicio = forms.DateField(label='Fecha de inicio')
    fecha_fin = forms.DateField(label='Fecha de fin')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha_inicio"].widget = forms.SelectDateWidget()
        self.fields["fecha_fin"].widget = forms.SelectDateWidget()


class SolicitudMovilizacionForm(forms.ModelForm):
    class Meta:
        model = Movilizacion
        fields = ['motivo', 'fecha_salida', 'hora_salida', 'ruta', 'kilometraje_inicio', 'personaModel', 'vehiculoModel', 'ocupantes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha_salida"].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields["hora_salida"].widget = forms.TextInput(attrs={'placeholder': 'HH:MM'})
    
#por si sale mal 

class ConsumoCombustibleForm(forms.ModelForm):
    class Meta:
        model = ConsumoCombustible
        fields = ['conductor', 'vehiculo', 'gasolinera', 'galones_combustible', 'fecha_hora', 'kilometraje_actual', 'fecha_solicitud']
        
