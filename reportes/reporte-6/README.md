<div align="center">

# 📊 Reporte Semana 6
### Marketplace Multivendedor Ecommerce

![Report](https://img.shields.io/badge/Report-Week%206-blue)
![Project](https://img.shields.io/badge/Project-Academic-lightgrey)

</div>

---

<div align="center">
  
## 🔗 Navegación rápida

🏠 [Repositorio principal](../../)
📊 [Índice de reportes](../)
📚 [Documentación](../../docs/)
🧪 [Pruebas](../../docs/pruebas/)
📐 [Diagramas UML](../../docs/uml/)

</div>

---

<a name="contenido"></a>

# 📑 Tabla de Contenidos

<div align="center">

<table>

<tr>

<td align="center" width="200">

### 📘 Introducción  
[Ir a sección](#introduccion)

</td>

<td align="center" width="200">

### 🎯 Objetivos  
[Ir a sección](#objetivos)

</td>

<td align="center" width="200">

### 🎬 Demo  
[Ir a sección](#demo)

</td>

</tr>

<tr>

<td align="center">

### 🏗 Arquitectura  
[Ir a sección](#arquitectura)

</td>

<td align="center">

### 🧩 Patrones  
[Ir a sección](#patrones)

</td>

<td align="center">

### 🔌 API  
[Ir a sección](#api)

</td>

</tr>

<tr>

<td align="center">

### 🧪 Pruebas  
[Ir a sección](#pruebas)

</td>

<td align="center">

### 🛠 Tecnologías  
[Ir a sección](#tecnologias)

</td>

<td align="center">

### 📂 Estructura  
[Ir a sección](#estructura)

</td>

</tr>

<tr>

<td align="center">

### ⚙ Metodología  
[Ir a sección](#metodologia)

</td>

<td align="center">

### 📚 Referencias  
[Ir a sección](#referencias)

</td>

<td align="center">

### 👨‍💻 Autores  
[Ir a sección](#autores)

</td>

</tr>

</table>

</div>

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
