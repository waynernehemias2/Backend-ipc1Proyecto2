from flask import Flask, jsonify, request
from flask_cors import CORS


from Persona import Persona
from  Cita import Cita
from Medicamento import Medicamento
from Factura import Factura
from Receta import Receta
from Compra import Compra

import json 

Personas = []
Citas = []
Medicamentos = []
Facturas =[]
Recetas = []
Compras = []
Personas.append(Persona('Carlos','Jimenez','01/01/2000','M','admin','1234',' ','01800','admin'))

logiado = ""
Npersona = ""
nomDoc = ""
bol = True
Est = "Pendiente"
Paso = "permitido"

app=Flask(__name__)
CORS(app)
 
@app.route('/', methods=['GET'])

def rutaInicial():
    return("<center><h1>Bienvenido</h1></center>")
 
@app.route('/', methods=['POST'])
def rutaPost():
    # En este caso creamos un Diccionario de Python, los diccionarios son listas de clave-valor
    # Si lo comparamos, puede adaptarse perfectamente como un objeto JSON.
    objeto = {"Mensaje":"Se hizo el POST correctamente"}
    # Utilizamos el jsonify para devolver el objeto JSON de manera ordenada
    return(jsonify(objeto))

 
@app.route('/Personas', methods=['GET'])
def getPersonas():
    # Tenemos nuestra lista en el entorno global, por eso hacemos referencia a ella con la palabra global
    global Personas
    # Creamos un arreglo de Python para almacenar la informacion
    Datos = []
    # Hacemos un recorrido de nuestro arreglo
    for persona in Personas:
        # Por cada objeto en nuestro arreglo, escribimos un objeto JSON, es decir clave-valor
        objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'FechaNacimiento': persona.getFechaNacimiento(),
            'Sexo': persona.getSexo(),
            'Usuario': persona.getUsuario(),
            'Contrasena': persona.getContrasena(),
            'Especialidad': persona.getEspecialidad(),
            'Telefono': persona.getTelefono(),
            'Tipo': persona.getTipo()
        }
        # Agregamos el dato encontrado a la lista creada anteriormente.
        Datos.append(objeto)
    # Le mandamos la informacion como respuesta, para este punto recorrio el arreglo y creo objetos JSON.    
    return(jsonify(Datos))

@app.route('/Citas', methods=['GET'])
def getCitas():
    global Citas
    Datos =[]
    for cita in Citas:
        objeto = {
            'Paciente': cita.getPaciente(),
            'Apellido': cita.getApellido(),
            'Usuario': cita.getUsuario(),
            'Fecha': cita.getFecha(),
            'Hora': cita.getHora(),
            'Motivo': cita.getMotivo(),
            'Estado': cita.getEstado(),
            'Doctor': cita.getDoctor(),
            'Nombre': cita.getNombre()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Compras', methods=['GET'])
def getCompras(): 
    global Compras
    Datos =[]
    for compra in Compras:
        objeto = {
            'Nombre': compra.getNombre(),
            'Cantidad': compra.getCantidad()
        }
        Datos.append(objeto)
    return(jsonify(Datos))
  
@app.route('/Recetas', methods=['GET'])
def getRecetas():
    global Recetas
    Datos =[]
    for receta in Recetas:
        objeto = {
            'fecha': receta.getFecha(),
            'paciente': receta.getPaciente(),
            'padecimiento': receta.getPadecimiento()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

 
@app.route('/VerCita/<string:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerCita(nombre): 
    # Referencia al arreglo global
    global Citas 
    # Recorrido del arreglo
    for cita in Citas:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if cita.getUsuario() == nombre:
            # Crear el objeto
            objeto = {
                'Paciente': cita.getPaciente(),
                'Apellido': cita.getApellido(),
                'Usuario': cita.getUsuario(),
                'Fecha': cita.getFecha(),
                'Hora': cita.getHora(),
                'Motivo': cita.getMotivo(),
                'Estado': cita.getEstado(),
                'Doctor': cita.getDoctor()
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))
    # Si llega a este punto, quiere decir que nunca entro al for, entonces creamos un objeto        
    salida = { "Mensaje": "No existe usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))
 
@app.route('/UsuarioP', methods=['GET'])
def getPaciente():
    # Tenemos nuestra lista en el entorno global, por eso hacemos referencia a ella con la palabra global
    global logiado
    global Npersona
    global Personas
    # Recorrido del arreglo
    for persona in Personas:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if persona.getUsuario() == logiado:
            # Crear el objeto
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'FechaNacimiento': persona.getFechaNacimiento(),
            'Sexo': persona.getSexo(),
            'Usuario': persona.getUsuario(),
            'Contrasena': persona.getContrasena(),
            'Especialidad': persona.getEspecialidad(),
            'Telefono': persona.getTelefono()
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))
    # Si llega a este punto, quiere decir que nunca entro al for, entonces creamos un objeto        
    salida = { "Mensaje": "No existe usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))
 
@app.route('/Medicamentos', methods=['GET'])
def getMedicamentos():
    # Tenemos nuestra lista en el entorno global, por eso hacemos referencia a ella con la palabra global
    global Medicamentos
    # Creamos un arreglo de Python para almacenar la informacion
    Datos = []
    # Hacemos un recorrido de nuestro arreglo
    for medicamento in Medicamentos:
        # Por cada objeto en nuestro arreglo, escribimos un objeto JSON, es decir clave-valor
        objeto = {
            'Nombre': medicamento.getNombre(),
            'Precio': medicamento.getPrecio(),
            'Descripcion': medicamento.getDescripcion(),
            'Cantidad': medicamento.getCantidad()
        }
        # Agregamos el dato encontrado a la lista creada anteriormente.
        Datos.append(objeto)
    # Le mandamos la informacion como respuesta, para este punto recorrio el arreglo y creo objetos JSON.    
    return(jsonify(Datos))

 
@app.route('/VerPersona/<string:nombre>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerPaciente(nombre): 
    # Referencia al arreglo global
    global Personas
    # Recorrido del arreglo
    for persona in Personas:
        # Si el objeto actual tiene el nombre que le mandamos como parametro entonces
        if persona.getUsuario() == nombre:
            # Crear el objeto
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'FechaNacimiento': persona.getFechaNacimiento(),
            'Sexo': persona.getSexo(),
            'Usuario': persona.getUsuario(),
            'Contrasena': persona.getContrasena(),
            'Especialidad': persona.getEspecialidad(),
            'Telefono': persona.getTelefono()
            }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
            return(jsonify(objeto))
    # Si llega a este punto, quiere decir que nunca entro al for, entonces creamos un objeto        
    salida = { "Mensaje": "No existe usuario con ese nombre"}
    # Retornamos el objeto creado
    return(jsonify(salida))



@app.route('/VerMedicamento/<int:ite>', methods=['GET'])
# Luego para definir el metodo, hay que agregar el nombreVar como parametro del metodo
def ObtenerMedicamento(ite): 
    # Referencia al arreglo global
    global Medicamentos
    # Recorrido del arreglo
            # Crear el objeto
    objeto = {
        'Nombre': Medicamentos[ite].getNombre(),
        'Precio': Medicamentos[ite].getPrecio(),
        'Descripcion': Medicamentos[ite].getDescripcion(),
        'Cantidad': Medicamentos[ite].getCantidad()
    }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
    return(jsonify(objeto))

@app.route('/navegar', methods=['GET'])
def paginas():
    global Paso
    objeto = {
        'permitir': Paso
    }
            # Como ya no necesitamos buscar mas, aplicamos el return para este punto
    return(jsonify(objeto)) 
 
@app.route('/navegar/<string:estado>', methods=['PUT'])
def paginascerrar(estado):
    global Paso
    Paso = estado
    Paso = request.json['permitir']
    return(jsonify({'Mensaje':'Sesion finalizada',}))

@app.route('/Inicio/<string:usuario>/<string:contrasena>', methods=['GET'])
def ObtenerInicio(usuario,contrasena): 
    global Personas
    global logiado
    global bol
    global Paso
    logiado = usuario
    encontrado = False
    print (logiado)
    for persona in Personas:
        if persona.getUsuario() == usuario and persona.getContrasena() == contrasena:
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'FechaNacimiento': persona.getFechaNacimiento(),
            'Sexo': persona.getSexo(),
            'Usuario': persona.getUsuario(),
            'Contrasena': persona.getContrasena(),
            'Especialidad': persona.getEspecialidad(),
            'Telefono': persona.getTelefono(),
            'Tipo' : persona.getTipo()
            }
            
            encontrado = True
            if encontrado == True:
                bol = True
                return(jsonify(objeto))
    Paso = "permitido"          
    return(jsonify({"mensaje": "No encontrado"}))

@app.route('/Recetas', methods=['POST'])
def AgregarReceta():
    # Referencia a la lista global
    global Recetas
    fecha = request.json['fecha']
    paciente = request.json['paciente']
    padecimiento = request.json['padecimiento']
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Receta(fecha,paciente,padecimiento)
    # Agregamos 
    Recetas.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se creo la receta exitosamente',})

@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    # Referencia a la lista global
    global Personas

    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fechaNacimiento = request.json['fechaNacimiento']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    especialidad = request.json['especialidad']
    telefono = request.json['telefono']
    tipo = request.json['tipo']
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Persona(nombre,apellido,fechaNacimiento,sexo,usuario,contrasena,especialidad,telefono,tipo)
    # Agregamos
    Personas.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})
 
@app.route('/Compras', methods=['POST'])
def AgregarCompra():
    # Referencia a la lista global
    global Compras

    nombre = request.json['nombre']
    cantidad = request.json['cantidad']
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Compra(nombre,cantidad)
    # Agregamos
    Compras.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})

@app.route('/CitasN', methods=['POST'])
def AgregarCita():
    # Referencia a la lista global
    global Citas
    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    paciente = request.json['paciente']
    apellido = request.json['apellido']
    usuario = request.json['usuario']
    fecha = request.json['fecha']
    hora = request.json['hora']
    motivo = request.json['motivo']
    estado = request.json['estado']
    doctor = request.json['doctor']
    nombre = request.json['nombre']
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Cita(paciente,apellido,usuario,fecha,hora,motivo,estado,doctor,nombre)
    # Agregamos la persona
    Citas.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego la cita exitosamente',})

@app.route('/Medicamentos', methods=['POST'])
def AgregarMedicamentos():
    # Referencia a la lista global
    global Medicamentos
    # Como mencioamos anteriormente, el cliente se debe de encargar de mandarle un body a la API para que
    # pueda manejar esta informacion, Flask almacena esta informacion en el request.
    # Para obtener la informacion usamos la siguiente sintaxis.
    # request.json['clave'], donde clave es un campo recibido del body mandado por el cliente
    # NOTA: Esta clave debe coincidir con el body del cliente, si no, nos dara error.
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    cantidad = request.json['cantidad']
    # Creamos nuestro nuevo objeto con la informacion recolectada del request
    nuevo = Medicamento(nombre,precio,descripcion,cantidad)
    # Agregamos la persona
    Medicamentos.append(nuevo)
    # Retornamos nuestro objeto JSON con la salida esperada
    return jsonify({'Mensaje':'Se agrego el medicamento exitosamente',})

@app.route('/cantidadMed/<string:medica>', methods=['PUT'])
def ActualizarCantidad(medica):
    # Hacemos referencia a nuestro usuario global
    global Medicamentos
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for m in range(len(Medicamentos)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if medica == Medicamentos[m].getNombre():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Medicamentos[m].setCantidad(request.json['cantidad'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se hizo la compra exitosamente',})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar',})
 
@app.route('/Personas/<string:usuario>', methods=['PUT'])
def ActualizarPersona(usuario):
    # Hacemos referencia a nuestro usuario global
    global Personas
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(Personas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if usuario == Personas[i].getUsuario():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Personas[i].setNombre(request.json['nombre'])
            Personas[i].setApellido(request.json['apellido'])
            Personas[i].setFechaNacimiento(request.json['fechaNacimiento'])
            Personas[i].setSexo(request.json['sexo'])
            Personas[i].setUsuario(request.json['usuario']) 
            Personas[i].setContrasena(request.json['contrasena'])
            Personas[i].setEspecialidad(request.json['especialidad'])
            Personas[i].setTelefono(request.json['telefono'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente',})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar',})

@app.route('/CitaAceptada/<string:usuario>/<string:doc>', methods=['PUT'])
def ActualizarCita(usuario,doc):
    # Hacemos referencia a nuestro usuario global
    global nomDoc
    global Personas
    global Citas
    global Est
            
    for x in range(len(Personas)):
        if doc == Personas[x].getUsuario():
            nomDoc = Personas[x].getNombre()
    for i in range(len(Citas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if Est == Citas[i].getEstado() and usuario == Citas[i].getUsuario():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Citas[i].setEstado(request.json['estado'])
            Citas[i].setDoctor(request.json['doctor'])
            Citas[i].setNombre(nomDoc)
            
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se Acepto la cita exitosamente',})
            
    # Si llega a este punto, quiere decir que salio del for
    
    return jsonify({'Mensaje':'No se pudo Aceptar',})

@app.route('/CitaRechazada/<string:usuario>', methods=['PUT'])
def RechazarCita(usuario):
    # Hacemos referencia a nuestro usuario global
    global Personas
    global Citas
    global Est
            
    for i in range(len(Citas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if Est == Citas[i].getEstado() and usuario == Citas[i].getUsuario():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Citas[i].setEstado(request.json['estado'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se Rechazo la cita exitosamente',})
            
    # Si llega a este punto, quiere decir que salio del for
    
    return jsonify({'Mensaje':'No se pudo Aceptar',}) 

@app.route('/CitaCompletada/<string:usuario>', methods=['PUT'])
def CompletarCita(usuario):
    # Hacemos referencia a nuestro usuario global
    global Personas
    global Citas
    global Est
            
    for i in range(len(Citas)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if Citas[i].getEstado() =="Aceptada" and usuario == Citas[i].getUsuario():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Citas[i].setEstado(request.json['estado'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se completo la cita exitosamente',})
            
    # Si llega a este punto, quiere decir que salio del for
    
    return jsonify({'Mensaje':'No se pudo Aceptar',})
 

@app.route('/MedicamentosActualizar/<string:nombre>', methods=['PUT'])
def ActualizarMedicamentos(nombre):
    # Hacemos referencia a nuestro usuario global
    global Medicamentos
    # Como queremos actualizar un dato en especifico, haremos un for un poco diferente
    # En este caso, si trabajaremos con el indice, donde range nos devuelve los numero de 0 hasta donde le indiquemos
    # En este caso, la longitud del arreglo
    for i in range(len(Medicamentos)):
        # Validamos si el nombre que le mandamos como parametro es el que queremos actualizar
        if nombre == Medicamentos[i].getNombre():
            # Con ayuda de los metodos SET creados en la clase, le asignamos el valor del request
            Medicamentos[i].setNombre(request.json['nombre'])
            Medicamentos[i].setPrecio(request.json['precio'])
            Medicamentos[i].setDescripcion(request.json['descripcion'])
            Medicamentos[i].setCantidad(request.json['cantidad'])
            # Mandamos el mensaje de informacion actualizada
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

# METODO - ELIMINAR UN DATO
# En este caso, como trabajaremos con un solo dato, podemos mandar la informacion como parametro.
# NOTA: NO ES NECESARIO UTILIZAR EL METHOD DELETE, ES REFERENCIA UNICAMENTE
@app.route('/PersonasEliminar/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    # Referencia al arreglo global
    global Personas
    # Usamos un for para manejar por medio del indice
    for i in range(len(Personas)):
        # Validamos si es el nombre que queremos
        if nombre == Personas[i].getUsuario():
            # Usamos del para eliminar el objeto
            del Personas[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for        
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

@app.route('/MedicamentosEliminar/<string:nombre>', methods=['DELETE'])
def EliminarMedicamentos(nombre):
    # Referencia al arreglo global
    global Medicamentos
    # Usamos un for para manejar por medio del indice
    for i in range(len(Medicamentos)):
        # Validamos si es el nombre que queremos
        if nombre == Medicamentos[i].getNombre():
            # Usamos del para eliminar el objeto
            del Medicamentos[i]
            # Mandamos el mensaje de la informacion eliminada
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    # Si llega a este punto, quiere decir que salio del for        
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug =True)

