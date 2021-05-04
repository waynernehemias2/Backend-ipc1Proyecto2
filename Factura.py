class Factura:
    def __init__(self,fecha,paciente,doctor,pconsulta,coperacion,cinternado,total):
        self.fecha = fecha
        self.paciente = paciente
        self.doctor = doctor
        self.pconsulta = pconsulta
        self.coperacion = coperacion
        self.cinternado = cinternado
        self.total = total

    def getFecha(self):
        return self.fecha 

    def getPaciente(self):
        return self.paciente

    def getDoctor(self):
        return self.doctor 

    def getPconsulta(self):
        return self.pconsulta 

    def getCoperacion(self):
        return self.coperacion 

    def getCinternado(self):
        return self.cinternado 

    def getTotal(self):
        return self.total 

    def setFecha(self, fecha):
        self.fecha = fecha

    def setPaciente(self, paciente):
        self.paciente = paciente

    def setDoctor(self, doctor):
        self.doctor = doctor

    def setPconsulta(self, pconsulta):
        self.pconsulta = pconsulta

    def setCoperacion(self, coperacion):
        self.coperacion = coperacion

    def setCinternado(self, cinternado):
        self.cinternado = cinternado

    def setTotal(self, total): 
        self.total = total