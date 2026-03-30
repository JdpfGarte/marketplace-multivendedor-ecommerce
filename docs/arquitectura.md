# 🏗 Arquitectura del Sistema

El sistema sigue una arquitectura basada en **API REST** utilizando **FastAPI** como framework principal para la construcción de los endpoints.

Esta arquitectura permite separar claramente las responsabilidades del sistema y facilitar su mantenimiento y escalabilidad.

## 🔧 Componentes principales

El sistema se compone de los siguientes elementos:

- **API REST**: interfaz que permite interactuar con el sistema mediante solicitudes HTTP.
- **Lógica de negocio**: encargada de gestionar la creación y administración de las obras.
- **Inventario del sistema**: estructura centralizada donde se almacenan todas las obras registradas.

## 🧩 Uso de patrones de diseño

Para mejorar la estructura del sistema se implementan **patrones de diseño creacionales**.

Estos patrones permiten desacoplar la creación de objetos y mejorar la extensibilidad del software.

Los patrones utilizados son:

- **Singleton**  
  Garantiza que exista una única instancia del inventario del sistema.

- **Factory Method**  
  Permite crear distintos tipos de obras sin acoplar la lógica a clases concretas.

- **Abstract Factory**  
  Facilita la creación de familias de objetos relacionadas, como obras físicas y digitales.

- **Builder**  
  Permite construir objetos complejos paso a paso agregando propiedades adicionales.

## 📐 Arquitectura general

La arquitectura del sistema puede representarse mediante un diagrama UML general ACTUALIZADO ubicado en:

```
docs/uml/uml_generalV2.png
```

Este diagrama permite visualizar la relación entre las clases y los patrones implementados.
