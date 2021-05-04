class Cita:
    def __init__(self,paciente,apellido,usuario,fecha,hora,motivo,estado,doctor,nombre):
        self.paciente = paciente
        self.apellido = apellido
        self.usuario = usuario
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
        self.doctor = doctor
        self.nombre = nombre

    def getPaciente(self):
        return self.paciente

    def getApellido(self):
        return self.apellido

    def getUsuario(self):
        return self.usuario

    def getFecha(self):
        return self.fecha

    def getHora(self):
        return self.hora

    def getMotivo(self):
        return self.motivo

    def getEstado(self):
        return self.estado

    def getDoctor(self):
        return self.doctor

    def getNombre(self):
        return self.nombre

    def setPaciente(self, paciente):
        self.paciente = paciente

    def setApellido(self, apellido):
        self.apellido = apellido

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setFecha(self, fecha):
        self.fecha = fecha

    def setHora(self, hora):
        self.hora = hora

    def setMotivo(self, motivo):
        self.motivo = motivo

    def setEstado(self, estado):
        self.estado = estado

    def setDoctor(self, doctor):
        self.doctor = doctor

    def setNombre(self, nombre):
        self.nombre = nombre