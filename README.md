# GIC - Gestión Integral de Clientes

Sistema simple de gestión de clientes desarrollado en Python.  
Permite registrar, validar y manejar clientes utilizando buenas prácticas como:

- Programación orientada a objetos
- Manejo de excepciones personalizadas
- Logging de eventos
- Arquitectura modular

---

## Características

- Registro de clientes
- Validación de datos
- Excepciones personalizadas
- Registro de eventos en archivo `.log`
- Código organizado y escalable

---

## Arquitectura del Proyecto

```
GIC/
│
├── main.py
├── cliente.py
├── errores.py
├── logger.py
└── README.md
```

---

## Descripción de Archivos

### main.py

Archivo principal del programa.  
Ejecuta la aplicación y gestiona el flujo general.

### cliente.py

Contiene la clase `Cliente` y la lógica para agregar o buscar clientes.

### errores.py

Define excepciones personalizadas:

```python
class ValidacionError(Exception):
    pass

class ClienteNoEncontradoError(Exception):
    pass
```

### logger.py

Configura el sistema de logging:

```python
import logging

logging.basicConfig(
    filename="gic.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar(mensaje):
    logging.info(mensaje)
```

---

## Ejemplo de Uso

### Agregar cliente

```python
clientes = []

def agregar_cliente(nombre):
    if not nombre:
        raise ValidacionError("El nombre no puede estar vacío")

    clientes.append(nombre)
    registrar(f"Cliente agregado: {nombre}")
```

### Buscar cliente

```python
def buscar_cliente(nombre):
    if nombre not in clientes:
        raise ClienteNoEncontradoError("Cliente no encontrado")

    return nombre
```

---

## Manejo de Excepciones

El sistema utiliza excepciones personalizadas para mejorar la claridad del código y el control de errores.

```python
try:
    agregar_cliente("")
except ValidacionError as e:
    print("Error de validación:", e)
```

---

## Logging

Todos los eventos importantes se registran automáticamente en:

```
gic.log
```

Formato del registro:

```
Fecha - Nivel - Mensaje
```

Ejemplo:

```
2026-02-14 08:15:23,456 - INFO - Cliente agregado: Bryan
```

---

## Buenas Prácticas Aplicadas

- Separación de responsabilidades
- Código modular
- Uso de excepciones específicas
- Registro de eventos
- Estructura clara y profesional
