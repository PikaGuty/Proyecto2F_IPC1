class Persona:
    def __init__(self,id,nombre,apellido,fechan,sexo,nombre_us,contraseña,especialidad,telefono,tipo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fechan = fechan 
        self.sexo = sexo
        self.nombre_us = nombre_us
        self.contraseña = contraseña 
        self.especialidad = especialidad
        self.telefono = telefono
        self.tipo = tipo

    # METODOS GET
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getFechan(self):
        return self.fechan

    def getSexo(self):
        return self.sexo

    def getNombre_us(self):
        return self.nombre_us

    def getContraseña(self):
        return self.contraseña

    def getEspecialidad(self):
        return self.especialidad

    def getTelefono(self):
        return self.telefono

    def getTipo(self):
        return self.tipo

    # METODOS SET
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setFechan(self,fechan):
        return self.fechan

    def setSexo(self,sexo):
        return self.sexo

    def setNombre_us(self,nombre_us):
        return self.nombre_us

    def setContraseña(self,contraseña):
        return self.contraseña

    def setEspecialidad(self,especialidad):
        return self.especialidad

    def setTelefono(self,telefono):
        return self.telefono

    def setTipo(self,tipo):
        return self.tipo