<div align="center">
  
<a href="https://github.com/JdpfGarte/marketplace-multivendedor-ecommerce/">
  <p align="center">
    <img src="/docs/banner.png" width="900">
  </p>
</a>

---

# 🎨 Sistema de Gestión de Inventario para Galería de Arte
### 🧩 Implementación de Patrones de Diseño Creacionales

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)
![UML](https://img.shields.io/badge/UML-Diagrams-orange)
![Design Patterns](https://img.shields.io/badge/Design%20Patterns-Singleton%20|%20Factory%20|%20Builder-blueviolet)
![Status](https://img.shields.io/badge/Status-Academic%20Project-lightgrey)

### 📚 Proyecto académico de Patrones de Software
### 🚀 API REST para gestión de obras físicas y digitales

</div>

---

# 🏷 Badges del Proyecto

## 🧰 Tecnologías

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)
![Swagger](https://img.shields.io/badge/Swagger-API%20Docs-brightgreen?logo=swagger)
![UML](https://img.shields.io/badge/UML-Diagrams-orange)
![Git](https://img.shields.io/badge/Git-Version%20Control-red?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

---

## 🧩 Patrones de Diseño

![Singleton](https://img.shields.io/badge/pattern-Singleton-purple)
![Factory Method](https://img.shields.io/badge/pattern-Factory%20Method-blue)
![Abstract Factory](https://img.shields.io/badge/pattern-Abstract%20Factory-orange)
![Builder](https://img.shields.io/badge/pattern-Builder-yellow)

---

## 🚦 Estado del Proyecto

![Status](https://img.shields.io/badge/status-active-green)
![Project](https://img.shields.io/badge/project-academic-lightgrey)
![Maintenance](https://img.shields.io/badge/maintained-yes-green)

---

<a name="contenido"></a>

# 📑 Tabla de Contenidos

- [📘 Introducción](#introduccion)
- [🎯 Objetivos](#objetivos)
- [🎬 Demo](#demo)
- [🏗 Arquitectura](#arquitectura)
- [🧩 Patrones de Diseño](#patrones)
- [🔌 API Endpoints](#api)
- [🧪 Pruebas](#pruebas)
- [🛠 Tecnologías](#tecnologias)
- [📂 Estructura](#estructura)
- [⚙ Metodología](#metodologia)
- [📚 Referencias](#referencias)
- [👨‍💻 Autores](#autores)

---

<a name="introduccion"></a>

# 📘 Introducción

Este proyecto corresponde a un **Sistema de Gestión de Inventario para una Galería de Arte Multiformato**.

El sistema permite gestionar:

🎨 Obras físicas  
💻 Obras digitales  

Se implementa como una **API REST utilizando FastAPI**.

⬆ [Volver al contenido](#contenido)

---

<a name="objetivos"></a>

# 🎯 Objetivos del Proyecto

✔ Implementar Singleton  
✔ Implementar Factory Method  
✔ Implementar Abstract Factory  
✔ Implementar Builder  

⬆ [Volver al contenido](#contenido)

---

<a name="demo"></a>

# 🎬 Demo del Sistema

## 💻 Creación de obra digital

<p align="center">
  <img src="/docs/pruebas/factory_method/factory_method1.png" width="310">
</p>

---

## 🖼 Creación de obra física

<p align="center">
  <img src="/docs/pruebas/factory_method/factory_method3.png" width="310">
</p>

---

## 📚 Consulta del catálogo

<p align="center">
  <img src="/docs/pruebas/singleton/singleton2.png" width="750">
</p>

⬆ [Volver al contenido](#contenido)

---

<a name="arquitectura"></a>

# 🏗 Arquitectura del Sistema

<p align="center">
  <img src="/docs/uml/uml_general.png" width="510">
</p>

⬆ [Volver al contenido](#contenido)

---

<a name="patrones"></a>

# 🧩 Patrones de Diseño Implementados

## 📊 Resumen de Patrones

| Patrón | Tipo | Propósito | Aplicación |
|------|------|------|------|
| Singleton | Creacional | Instancia única | Inventario global |
| Factory Method | Creacional | Crear objetos | Obras |
| Abstract Factory | Creacional | Familias de objetos | Físico / Digital |
| Builder | Creacional | Construcción paso a paso | Configuración |

---

## Singleton

```
python
class inventariosistema:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.lista_obras = []
        return cls._instancia
```

---

## Factory Method

```
python
class fabricafisica:
    @staticmethod
    def crear(...):
        return obrafisica(...)

class fabricadigital:
    @staticmethod
    def crear(...):
        return obradigital(...)
```

---

## Builder

```
python
class obrabuilder:

    def con_certificado(self, valor):
        self.obra.certificado = valor
        return self
```

---

<a name="api"></a>

# 🔌 API Endpoints

| Método | Endpoint | Descripción |
|------|------|------|
| GET | /catalogo | Obtener catálogo |
| GET | /recomendar/{obra_id} | Recomendar obras |
| POST | /nuevo_producto | Crear obra |

⬆ [Volver al contenido](#contenido)

---

<a name="pruebas"></a>

# 🧪 Pruebas del Sistema

Las evidencias se encuentran en:

| Patrón | Evidencia |
|------|------|
| Singleton | [Visualizar](docs/pruebas/singleton) |
| Factory Method | [Visualizar](docs/pruebas/factory_method) |
| Abstract Factory | [Visualizar](docs/pruebas/abstract_factory) |
| Builder | [Visualizar](docs/pruebas/builder) |

⬆ [Volver al contenido](#contenido)

---

<a name="tecnologias"></a>

# 🛠 Tecnologías Utilizadas

| Tecnología | Uso |
|------|------|
| Python | Lenguaje |
| FastAPI | API |
| Swagger | Documentación |
| UML | Arquitectura |
| GitHub | Control de versiones |

⬆ [Volver al contenido](#contenido)

---

<a name="estructura"></a>

# 📂 Estructura del Proyecto

```
marketplace-multivendedor-ecommerce/
│
├── main.py
├── models.py
├── README.md
│
├── docs/
│   ├── arquitectura.md
│   ├── modelo-conceptual.md
│   ├── requerimientos.md
│   ├── roadmap.md
│   │
│   ├── uml/
│   │   └── uml_general.png
│   │
│   └── pruebas/
│       ├── singleton/
│       ├── factory_method/
│       ├── abstract_factory/
│       └── builder/
```

⬆ [Volver al contenido](#contenido)

---

<a name="metodologia"></a>

# ⚙ Metodología

1. Análisis del problema  
2. Diseño UML  
3. Implementación FastAPI  
4. Integración de patrones  
5. Pruebas Swagger  

⬆ [Volver al contenido](#contenido)

---

<a name="referencias"></a>

# 📚 Referencias

La principal referencia teórica utilizada para el desarrollo y comprensión de los patrones de diseño implementados en este proyecto fue el siguiente documento académico:
```
Sánchez, G. (2025). Patrones de diseño y estrategias reutilizables en la
automatización de pruebas de software con Selenium y Java–Page Object Model,
Singleton, Factory y Fluent Interface. Revista Politécnica de Aguascalientes, 5.
```

⬆ [Volver al contenido](#contenido)

---

<a name="autores"></a>

# 👨‍💻 Autores

Jesús David Pérez Florian  
Andrés Felipe Florez Pérez

⬆ [Volver al contenido](#contenido)
