class Receta:
    def __init__(self,fecha,paciente,padecimiento):
        self.fecha = fecha
        self.paciente = paciente
        self.padecimiento = padecimiento

    def getFecha(self):
        return self.fecha 

    def getPaciente(self):
        return self.paciente

    def getPadecimiento(self):
        return self.padecimiento 


    def setFecha(self, fecha):
        self.fecha = fecha

    def setPaciente(self, paciente):
        self.paciente = paciente

    def setPadecimiento(self, padecimiento):
        self.padecimiento = padecimiento
