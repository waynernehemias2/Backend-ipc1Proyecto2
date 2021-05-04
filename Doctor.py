class Doctor:
    def __init__(self,nombreD,apellidoD,fechaNacimientoD,sexoD,usuarioD,contrasenaD,especialidadD,telefonoD):
        self.nombreD = nombreD
        self.apellidoD = apellidoD
        self.fechaNacimientoD = fechaNacimientoD
        self.sexoD = sexoD
        self.usuarioD = usuarioD
        self.contrasenaD = contrasenaD
        self.especialidadD = especialidadD
        self.telefonoD = telefonoD

    def getNombreD(self):
        return self.nombreD

    def getApellidoD(self):
        return self.apellidoD

    def getFechaNacimientoD(self):
        return self.fechaNacimientoD

    def getSexoD(self):
        return self.sexoD

    def getUsuarioD(self):
        return self.usuarioD
    
    def getContrasenaD(self):
        return self.contrasenaD

    def getEspecialidadD(self):
        return self.especialidadD

    def getTelefonoD(self):
        return self.telefonoD

    def setNombreD(self, nombreD):
        self.nombreD = nombreD

    def setApellidoD(self, apellidoD):
        self.apellidoD = apellidoD

    def setFechaNacimientoD(self, fechaNacimientoD):
        self.fechaNacimientoD= fechaNacimientoD

    def setSexoD(self, sexoD):
        self.sexoD = sexoD

    def setUsuarioD(self, usuarioD):
        self.usuarioD = usuarioD

    def setContrasenaD(self, contrasenaD):
        self.contrasenaD = contrasenaD

    def setEspecialidadD(self, especialidadD):
        self.especialidadD = especialidadD

    def setTelefonoD(self, telefonoD):
        self.telefonoD = telefonoD