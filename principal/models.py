from django.db import models


class personaModel(models.Model):
    cedula = models.CharField(max_length=20, null=True, blank=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    ciudad_nacimiento = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    idtiposangre = models.ForeignKey(
        "tiposangre", on_delete=models.CASCADE, null=True, blank=True)
    idrango = models.ForeignKey(
        "rango", on_delete=models.CASCADE, null=True, blank=True)
    idsubCircuito = models.ForeignKey(
        "SubCircuito", on_delete=models.CASCADE, null=True, blank=True)

    # Agregar campo para el vehículo asignado a la persona
    vehiculo_asignado = models.ForeignKey(
        "vehiculoModel", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"Cédula: {self.cedula} | Nombres: {self.nombres} | Apellidos: {self.apellidos}"


class tiposangre(models.Model):
    def __str__(self) -> str:
        return self.nombre
    nombre = models.CharField(max_length=100)


class rango(models.Model):
    def __str__(self) -> str:
        return self.nombre
    nombre = models.CharField(max_length=100)


class vehiculoModel(models.Model):
    
    placa = models.CharField(max_length=10, null=True)
    chasis = models.CharField(max_length=50, null=True)
    marca = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    motor = models.CharField(max_length=100, null=True)
    kilometraje = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    cilindraje = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    capacidad_carga = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    capacidad_pasajeros = models.PositiveIntegerField(null=True)

    idsubCircuito = models.ForeignKey("subCircuito", on_delete=models.CASCADE)
    idtipoVehiculo = models.ForeignKey("tipoVehiculo", on_delete=models.CASCADE)
    idtipoCombustible = models.ForeignKey("tipoCombustible", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Placa: {self.placa} |  Marca: {self.marca}'

class dependencia(models.Model):

    nombre = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.nombre}' + (f'({self.provincia})' if self.provincia != self.nombre else '')


class circuito(models.Model):

    nombreCircuito = models.CharField(max_length=100)
    nombreParroquia = models.CharField(max_length=100)
    iddependencia = models.ForeignKey(dependencia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nombreCircuito}' + (f' / {self.nombreParroquia}' if self.nombreParroquia != self.nombreCircuito else '') + f', {self.iddependencia}'


class subCircuito(models.Model):
    def __str__(self) -> str:

        return self.nombreSubCircuito
    nombreSubCircuito = models.CharField(max_length=100)
    idCircuito = models.ForeignKey(circuito, on_delete=models.CASCADE)


class tipoVehiculo(models.Model):
    def __str__(self) -> str:

        return self.nombreVehiculo
    nombreVehiculo = models.CharField(max_length=100)

class tipoCombustible(models.Model):
    def __str__(self) -> str:

        return f'{self.nombre} / {self.octanaje}'

    nombre = models.CharField(max_length=100)
    octanaje = models.IntegerField()  # O el tipo de campo que represente el octanaje

class tipoMantenimiento(models.Model):
    def __str__(self) -> str:

        return self.nombre
    nombre = models.CharField(max_length=100)


class mantenimiento(models.Model):
    def __str__(self) -> str:

        return f'{self.fecha} / {self.descripcion} / {self.idvehiculo} / {self.idtipomantenimiento}'
    
    fecha = models.DateField(null=True)
    descripcion = models.TextField()
    idvehiculo = models.ForeignKey('vehiculoModel', on_delete=models.CASCADE)
    idtipomantenimiento = models.ForeignKey(tipoMantenimiento, on_delete=models.CASCADE)
    
#repaso examen #

class Movilizacion(models.Model):
    motivo = models.TextField(null=True)
    fecha_salida = models.DateField(null=True)
    hora_salida = models.CharField(max_length=8, null=True)
    ruta = models.TextField(null=True)
    kilometraje_inicio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    personaModel = models.ForeignKey("personaModel", on_delete=models.CASCADE, null=True)
    vehiculoModel = models.ForeignKey("vehiculoModel", on_delete=models.CASCADE, null=True)
    ocupantes = models.TextField(null=True)

    def __str__(self):
        return f'Movilización - ID: {self.id}, Motivo: {self.motivo}'
    
#intento de orden de combustiblwe
class RegistroCombustible(models.Model):
    conductor = models.ForeignKey(personaModel, on_delete=models.CASCADE, related_name='registros_combustible_conductor')
    vehiculo = models.ForeignKey(vehiculoModel, on_delete=models.CASCADE, related_name='registros_combustible_vehiculo')
    solicitante = models.ForeignKey(personaModel, on_delete=models.CASCADE, related_name='registros_combustible_solicitante')
    gasolinera = models.CharField(max_length=100)
    galones_combustible = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(null=True)
    hora = models.CharField(max_length=8, null=True)
    kilometraje_actual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_solicitud = models.DateField(null=True)

    def __str__(self):
        return f"Registro de Combustible - Conductor: {self.conductor.nombres} {self.conductor.apellidos}, Vehículo: {self.vehiculo.placa}, Fecha: {self.fecha}"