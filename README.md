# GIC – Sistema de Gestión de Clientes

Proyecto desarrollado en **Python 3** aplicando principios sólidos de **Programación Orientada a Objetos (POO)**, arquitectura modular y patrón **CRUD**, incorporando validaciones, manejo de excepciones y sistema de logging.

---

## Descripción

GIC (Gestión Integral de Clientes) es una aplicación de consola diseñada para administrar distintos tipos de clientes mediante una estructura escalable, mantenible y orientada a buenas prácticas de ingeniería de software.

El sistema separa claramente:

- Modelo de dominio  
- Lógica de negocio  
- Validaciones  
- Manejo de excepciones  
- Interfaz de usuario  

Esta organización permite mejorar la mantenibilidad, facilitar futuras extensiones y garantizar una arquitectura limpia.

---

## Arquitectura del Proyecto


GIC/
│
├── modelos/
│ ├── cliente.py
│ ├── tipos_cliente.py
│
├── servicios/
│ ├── validaciones.py
│
├── excepciones.py
├── main.py
├── gic.log
└── README.md


---

## Estructura Modular

- **modelos/**  
  Contiene las entidades del dominio y la jerarquía de clases.

- **servicios/**  
  Incluye validaciones reutilizables y lógica auxiliar.

- **excepciones.py**  
  Define excepciones personalizadas del sistema.

- **main.py**  
  Punto de entrada de la aplicación. Gestiona la interacción con el usuario.

- **gic.log**  
  Archivo de registro de eventos del sistema.

---

## Principios de Ingeniería Aplicados

### Encapsulación

Uso de `@property` para proteger y validar atributos sensibles como `email` y `telefono` antes de su asignación, garantizando integridad de datos.

### Herencia

Las clases:

- `ClienteRegular`  
- `ClientePremium`  
- `ClienteCorporativo`  

heredan de la clase base `Cliente`.

### Polimorfismo

Cada subclase redefine los métodos:

- `tipo()`  
- `descuento()`  

Esto permite que el sistema trate a todos los clientes de manera uniforme, pero con comportamientos específicos según su tipo.

### Manejo de Excepciones

Se implementan excepciones personalizadas:

- `ValidacionError`  
- `ClienteNoEncontradoError`  

Esto mejora la robustez y claridad del sistema.

### Logging

Se utiliza el módulo estándar `logging` de Python para registrar eventos en el archivo `gic.log`, permitiendo trazabilidad y auditoría sin afectar la ejecución normal del programa.

---

## Funcionalidades Implementadas (CRUD)

La clase `GestorClientes` implementa el patrón CRUD:

| Operación | Método | Descripción |
|-----------|--------|------------|
| Create | `agregar()` | Agrega cliente validando duplicados |
| Read | `listar()` / `buscar()` | Consulta clientes |
| Update | `actualizar()` | Modifica atributos dinámicamente |
| Delete | `eliminar()` | Elimina cliente de forma segura |

---

## Ejecución del Proyecto

### Requisitos

- Python 3.x

### Ejecutar la aplicación

```bash
python main.py
Ejemplo de Uso
1. Agregar
2. Listar
3. Salir

El sistema gestiona distintos tipos de clientes aplicando polimorfismo de manera automática.

Diseño Técnico

Arquitectura limpia y modular

Separación clara de responsabilidades

Código extensible

Preparado para migrar a base de datos

Base sólida para futura implementación de API REST

Roadmap / Mejoras Futuras

Persistencia con MySQL o PostgreSQL

Implementación de API REST con FastAPI

Sistema de autenticación y roles

Incorporación de pruebas unitarias

Autor

Bryan William Nichol Poblete
Proyecto académico – Programación Orientada a Objetos

Licencia

Uso académico y educativo.

Conclusión

Este proyecto demuestra aplicación práctica de:

Programación Orientada a Objetos

Arquitectura modular

Buenas prácticas de diseño

Escalabilidad y mantenibilidad


---

Ahora sí:  
✔ GitHub lo interpretará perfectamente  
✔ La estructura se verá alineada  
✔ Las tablas funcionarán  
✔ Los bloques de código se verán correctamente  

Si quieres, puedo ahora dejarte una **versión aún más profesional estilo repositorio senior (con tabla de contenidos automática y sección de decisiones arquitectónicas)**.
