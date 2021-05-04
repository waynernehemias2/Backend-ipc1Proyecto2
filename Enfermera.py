class Enfermera:
    def __init__(self,nombreE,apellidoE,fechaNaciminetoE,sexoE,usuarioE,contrasenaE,telefonoE):
        self.nombreE = nombreE
        self.apellidoE = apellidoE
        self.fechaNacimientoE = fechaNaciminetoE
        self.sexo = sexoE
        self.usuario = usuarioE
        self.contrasena = contrasenaE
        self.telefono = telefonoE

    def getNombreE(self):
        return self.nombreE

    def getApellidoE(self):
        return self.apellidoE

    def getFechaNacimientoE(self):
        return self.fechaNacimientoE

    def getSexoE(self):
        return self.sexoE   
    
    def getUsuarioE(self):
        return self.usuarioE

    def getContrasenaE(self):
        return self.contrasenaE

    def getTelefonoE(self):
        return self.telefonoE

    def setNombreE(self, nombreE):
        self.nombreE = nombreE

    def setApellidoE(self, apellidoE):
        self.apellidoE = apellidoE

    def setFechaNacimientoE(self, fechaNacimientoE):
        self.fechaNacimientoE = fechaNacimientoE

    def setSexoE(self,sexoE):
        self.sexoE = sexoE

    def setUsuarioE(self, usuarioE):
        self.usuarioE = usuarioE

    def setContrasenaE(self, contrasenaE):
        self.contrasenaE = contrasenaE

    def setTelefonoE(self, telefonoE):
        self.telefonoE = telefonoE