# EstacionaMAX

Sistema autónomo de estacionamiento que permite realizar cobros automáticos en base al tiempo de permanencia y al tipo de vehículo.

El sistema permite gestionar:

* Vehículos
* Clientes
* Estacionamientos
* Categorías
* Registros de ingreso y salida

---

# Integrantes

* Fabrizio Rossato
* Lautaro Tonini

---

# Configuración del archivo `.env`

```env
MYSQL_USER=nombre_de_usuario
MYSQL_PASSWORD=contraseña
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_DATABASE=nombre_de_la_base_de_datos
```

---

# Ejecución del proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/LautaroTonini/app_estacionamiento
```

## 2. Ingresar al directorio del proyecto

```bash
cd app_estacionamiento
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Ejecutar la aplicación

```bash
python app.py
```

---

# Endpoints implementados

## Categorías

* `GET /api/categories` → Obtener todas las categorías
* `GET /api/categories/<nombre>` → Obtener categoría por nombre
* `POST /api/categories/add` → Agregar categoría
* `DELETE /api/categories/delete/<categoria>` → Eliminar categoría

---

## Clientes

* `GET /api/clients` → Obtener todos los clientes
* `GET /api/clients/<id>` → Obtener cliente por ID
* `POST /api/clients/add` → Agregar cliente
* `DELETE /api/clients/delete/<id>` → Eliminar cliente

---

## Vehículos

* `GET /api/vehicles` → Obtener todos los vehículos
* `POST /api/vehicles/create` → Agregar vehículo

---

## Localización / Estacionamientos

* `GET /api/locations` → Obtener todos los estacionamientos
* `GET /api/locations/<num_espacio>` → Obtener estacionamiento por número
* `GET /api/locations/empty` → Obtener un estacionamiento vacío
* `POST /api/locations/occupy/<num_espacio>` → Ocupar estacionamiento
* `POST /api/locations/vacate/<num_espacio>` → Desocupar estacionamiento

---

## Registros

* `POST /api/registers/create/<patente>` → Crear registro de ingreso
* `PUT /api/registers/finish/<patente>` → Finalizar registro de ingreso

---

# Aportes por integrante

## Lautaro Tonini

**Rama utilizada:** `Feature/LautaroTonini`

### Aportes

* App base
* Verificación de base de datos
* Gestión y conexión a base de datos
* Corrección de errores y formato
* Routes y controllers:

  * Comisión (`comision`)
  * Registro (`register`)

---

## Fabrizio Rossato

**Rama utilizada:** `Feature/FabrizioRossato`

### Aportes

* App base
* Edición del README
* Modelos, routes y controllers:

  * Cliente (`client`)
  * Vehículo (`vehicle`)
  * Ubicación (`location`)
  * Comisión (`comision`)
  * Registro (`register`)
  * Categoría (`category`)

---

# Tecnologías utilizadas

* Flask
* SQLAlchemy
* MySQL
* Postman
* Git
* GitHub
