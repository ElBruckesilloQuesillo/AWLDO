from django.db import models

# Create your models here.
class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=100)
    url_imagen = models.CharField(max_length=250)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre_ciudad)

class Destino(models.Model):
    id_destino = models.AutoField(primary_key=True)
    ciudad_destino = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    hora_llegada = models.TimeField()

    def __str__(self):
        texto = "Destino: {0} | Llegada: {1}"
        return texto.format(self.ciudad_destino,self.hora_llegada)

class Origen(models.Model):
    id_origen = models.AutoField(primary_key=True)
    ciudad_origen = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    hora_salida = models.TimeField()

    def __str__(self):
        texto = "Origen: {0} | Salida: {1}"
        return texto.format(self.ciudad_origen,self.hora_salida)

class Autobus(models.Model):
    id_autobus = models.AutoField(primary_key=True)
    placa_autobus = models.CharField(max_length=6)

    def __str__(self):
        texto = "Autobús: {0} | Placas: {1}"
        return texto.format(self.id_autobus,self.placa_autobus)
    

class Asiento(models.Model):
    id_asiento = models.AutoField(primary_key=True)
    asiento_ocupado = models.BooleanField(default=False)
    id_autobus = models.ForeignKey(Autobus, on_delete=models.CASCADE)

    def __str__(self):
        texto = "Asiento ({0}) | {2}"
        return texto.format(self.id_asiento, self.asiento_ocupado, self.id_autobus)



class Chofer(models.Model):
    id_chofer = models.AutoField(primary_key=True)
    nombre_chofer = models.CharField(max_length=50)
    ape_pat_chofer = models.CharField(max_length=50)
    ape_mat_chofer = models.CharField(max_length=50)
    telefono_chofer = models.CharField(max_length=10)

    def __str__(self):
        texto = "{0} {1} {2}"
        return texto.format(self.nombre_chofer, self.ape_pat_chofer, self.ape_mat_chofer)

class Viaje(models.Model):
    id_viaje = models.AutoField(primary_key=True)
    fecha_viaje = models.DateField()
    id_destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    id_origen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    id_autobus = models.ForeignKey(Autobus, on_delete=models.CASCADE)
    id_chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} --> {1}"
        return texto.format(self.id_origen, self.id_destino)