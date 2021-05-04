class Persona:
    def __init__(self,nombre,apellido,fechaNacimineto,sexo,usuario,contrasena,especialidad,telefono,tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimineto
        self.sexo = sexo
        self.usuario = usuario
        self.contrasena = contrasena
        self.especialidad = especialidad
        self.telefono = telefono
        self.tipo = tipo

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def getSexo(self):
        return self.sexo   
    
    def getUsuario(self):
        return self.usuario

    def getContrasena(self):
        return self.contrasena

    def getEspecialidad(self):
        return self.especialidad

    def getTelefono(self):
        return self.telefono

    def getTipo(self):
        return self.tipo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento

    def setSexo(self,sexo):
        self.sexo = sexo

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContrasena(self, contrasena):
        self.contrasena = contrasena

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def setTipo(self, tipo):
        self.tipo = tipo