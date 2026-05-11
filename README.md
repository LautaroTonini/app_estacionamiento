EstacionaMAX

Integrantes:
 • Lautaro Tonini
 • Fabrizio Rossato
 

Esta app es un sistema autonomo de estacionamiento, que permite un cobro automatico en base al tiempo de estacionamiento yal tipo de vehiculo ,El sistema permite gestionar vehiculos,cliente y etacionamientos

configuraciondel .env:
MYSQL_USER = (nombre de usuario)
MYSQL_PASSWORD = (contraseña)
MYSQL_HOST = 127.0.0.1
MYSQL_PORT = 330
MYSQL_DATABASE = (nombre de la DataBase)

Ejecucion del Proyecto

1.Clonar repositorio
    git clone https://github.com/LautaroTonini/app_estacionamiento
2.Ingresar al repositorio
    cd app_estacionamiento
3.Instalar dependencias
    pip install -r requirements.txt
4.Ejecutar
    python app.py

ENDPOINTS implementados:
    -Category: 
     •GET /api/categories (obtener todas las categorias)
     •GET /api/categories/<nombre> (obtener categorias por nombre)
     •GET /api/categories/add (agregar categoria)
     •DELETE /api/categories/delete/<categoria> (Eliminar categoria)
    -Clients:
     •GET /api/clients (Obtener todos los clientes)
     •GET /api/clients/<id> (Obtener cliente por id)
     •GET /api/clients/add (agregar Cliente)
     •DELETE /api/clients/delete/<id> (Eliminar cliente)
     -Vehiculos:
     •GET /api/vehicles (Obtener todos los vehículos)
     •GET/api/vehicles/create (agregar vehículo)
     -localizacion:
     •GET /api/locations (Obtener todos los estacionamientos)
     •GET /api/locations/<num_espacio> (Obtener un estacionamiento por número)
    -registros
     •GET /api/registers/create/<patente> (Crear un registro de ingreso utilizando patente)
     •PUT /api/registers/finish/<patente> (Finalizar un registro de ingreso)

Aportes por integrante:

• Lautaro Tonini:
    Rama utilizada:Feature/LautaroTonini
    - App base
    - Verificacion de base de datos
    - Gestion y coneccion a Base de datos
    - routes y controllers
        comision    (comision)
        registro    (register)
    - Correcion de errores / formato
    
• Fabrizio Rossato
    Rama utilizada:Feature/FabrizioRossato
    - App base
    -edicion READMI:md
    - Modelos,routes y controllers
        cliente     (client)
        vehiculo    (vehicle)
        ubicacion   (location)
        comision    (comision)
        registro    (register)
        categoria   (category)

