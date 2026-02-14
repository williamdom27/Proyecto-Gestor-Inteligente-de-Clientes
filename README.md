GIC – Sistema de Gestión de Clientes










Proyecto desarrollado en Python 3 aplicando principios sólidos de Programación Orientada a Objetos, arquitectura modular y patrón CRUD, con validaciones y sistema de logging.

 Descripción

GIC (Gestión Integral de Clientes) es una aplicación de consola diseñada para administrar clientes de distintos tipos mediante una estructura escalable y mantenible.

El sistema fue desarrollado bajo buenas prácticas de diseño de software, separando claramente:

Modelo de dominio

Lógica de negocio

Validaciones

Manejo de excepciones

Interfaz de usuario

 Arquitectura del Proyecto
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

modelos/ → Entidades del dominio

servicios/ → Validaciones reutilizables

excepciones.py → Excepciones personalizadas

main.py → Punto de entrada (interfaz)

gic.log → Registro de eventos

Principios de Ingeniería Aplicados
Encapsulación

Uso de @property para proteger y validar atributos sensibles como email y teléfono.

Herencia

Las clases:

ClienteRegular

ClientePremium

ClienteCorporativo

heredan de Cliente.

Polimorfismo

Cada subclase redefine:

tipo()

descuento()

permitiendo comportamiento dinámico sin modificar la lógica central.

⚠ Manejo de Excepciones

Se implementan excepciones personalizadas:

ValidacionError

ClienteNoEncontradoError

Mejora la robustez y claridad del sistema.

Logging

Uso del módulo logging para registrar eventos en gic.log, permitiendo trazabilidad y auditoría.

Funcionalidades (CRUD)

Implementadas en GestorClientes:

Operación	Método	Descripción
Create	agregar()	Añade cliente validando duplicados
Read	listar() / buscar()	Consulta clientes
Update	actualizar()	Modifica atributos dinámicamente
Delete	eliminar()	Elimina cliente de forma segura


Ejecutar aplicación
python main.py
Ejemplo de Uso
1. Agregar
2. Listar
3. Salir

El sistema gestiona distintos tipos de cliente aplicando polimorfismo automáticamente.

Diseño Técnico

Arquitectura limpia y modular

Separación de responsabilidades

Código extensible

Preparado para migrar a base de datos

Base sólida para API REST futura

Roadmap / Mejoras Futuras

Persistencia con MySQL o PostgreSQL

API REST con FastAPI

Autenticación y roles

Autor

Bryan William Nichol Poblete
Proyecto académico – Programación Orientada a Objetos

Licencia

Uso académico y educativo.

Conclusión

Este proyecto demuestra aplicación práctica de:

-Programación Orientada a Objetos
-Arquitectura modular
-Buenas prácticas de diseño
-Escalabilidad y mantenibilidad
