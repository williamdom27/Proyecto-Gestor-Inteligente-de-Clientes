GIC – Sistema de Gestión de Clientes

Proyecto desarrollado en Python 3 aplicando principios sólidos de Programación Orientada a Objetos (POO), arquitectura modular y patrón CRUD, incorporando validaciones, manejo de excepciones y sistema de logging.

1. Descripción

GIC (Gestión Integral de Clientes) es una aplicación de consola diseñada para administrar distintos tipos de clientes mediante una estructura escalable, mantenible y orientada a buenas prácticas de ingeniería de software.

El sistema fue desarrollado separando claramente las responsabilidades en:

Modelo de dominio

Lógica de negocio

Validaciones

Manejo de excepciones

Interfaz de usuario

Esta separación permite mejorar la mantenibilidad, facilitar futuras extensiones y garantizar una arquitectura limpia.

2. Arquitectura del Proyecto
GIC/
│
├── modelos/
│   ├── cliente.py
│   ├── tipos_cliente.py
│
├── servicios/
│   ├── validaciones.py
│
├── excepciones.py
├── main.py
├── gic.log
└── README.md
Estructura Modular

modelos/
Contiene las entidades del dominio y la jerarquía de clases.

servicios/
Incluye validaciones reutilizables y lógica auxiliar.

excepciones.py
Define excepciones personalizadas del sistema.

main.py
Punto de entrada de la aplicación. Gestiona la interacción con el usuario.

gic.log
Archivo de registro de eventos del sistema.

3. Principios de Ingeniería Aplicados
Encapsulación

Se implementa mediante el uso de @property para proteger atributos sensibles como email y telefono, validando su contenido antes de asignarlo.
Esto garantiza integridad de datos y control sobre el estado interno del objeto.

Herencia

Las clases:

ClienteRegular

ClientePremium

ClienteCorporativo

heredan de la clase base Cliente, reutilizando estructura y comportamiento común.

Polimorfismo

Cada subclase redefine los métodos:

tipo()

descuento()

Esto permite que el sistema trate a todos los clientes de manera uniforme, pero con comportamientos específicos según su tipo.

Manejo de Excepciones

Se implementan excepciones personalizadas:

ValidacionError

ClienteNoEncontradoError

Esto mejora la robustez del sistema y permite un control más preciso de errores.

Logging

Se utiliza el módulo estándar logging de Python para registrar eventos en el archivo gic.log.
El sistema permite trazabilidad, auditoría y diagnóstico sin afectar la ejecución normal del programa.

4. Funcionalidades Implementadas (CRUD)

La clase GestorClientes implementa el patrón CRUD:

Operación	Método	Descripción
Create	agregar()	Agrega cliente validando duplicados
Read	listar() / buscar()	Consulta clientes
Update	actualizar()	Modifica atributos dinámicamente
Delete	eliminar()	Elimina cliente de forma segura
5. Ejecución del Proyecto
Requisitos

Python 3.x

Ejecutar la aplicación
python main.py
6. Ejemplo de Uso
1. Agregar
2. Listar
3. Salir

El sistema gestiona distintos tipos de clientes aplicando polimorfismo de manera automática.

7. Diseño Técnico

Arquitectura limpia y modular

Separación clara de responsabilidades

Código extensible

Preparado para migrar a base de datos

Base sólida para futura implementación de API REST

8. Roadmap / Mejoras Futuras

Persistencia con MySQL o PostgreSQL

Implementación de API REST con FastAPI

Sistema de autenticación y roles

Incorporación de pruebas unitarias

9. Autor

Bryan William Nichol Poblete
Proyecto académico – Programación Orientada a Objetos

10. Licencia

Uso académico y educativo.

Conclusión

Este proyecto demuestra aplicación práctica de:

Programación Orientada a Objetos

Arquitectura modular

Buenas prácticas de diseño

Escalabilidad y mantenibilidad
