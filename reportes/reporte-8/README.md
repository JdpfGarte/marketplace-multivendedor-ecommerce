<div align="center">

# 📊 Reporte Semana 8
### Marketplace Multivendedor Ecommerce

![Report](https://img.shields.io/badge/Report-Week%208-blue)
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

Este proyecto corresponde a un **Sistema de Gestión de Inventario para una Galería de Arte Multiformato dentro de un Marketplace Multivendedor**.

El sistema permite gestionar:

🎨 Obras físicas  
💻 Obras digitales  
🧬 Clonación de obras  
🔐 Verificación de autenticidad  
🌐 Exportación a plataformas externas  

Se implementa como una **API REST utilizando FastAPI**, integrando múltiples patrones de diseño.

⬆ [Volver al contenido](#contenido)

---

<a name="objetivos"></a>

# 🎯 Objetivos del Proyecto

✔ Implementar Singleton  
✔ Implementar Factory Method  
✔ Implementar Abstract Factory  
✔ Implementar Builder  
✔ Implementar Prototype  
✔ Implementar Adapter  

⬆ [Volver al contenido](#contenido)

---

<a name="demo"></a>

# 🎬 Demo del Sistema

## 💻 Creación de obra digital

<p align="center">
  <img src="/docs/pruebas/factory_method/factory_method1.png" width="310">
</p>

---

## 🧬 Clonación de obra

<p align="center">
  <img src="/docs/pruebas/prototype/prototype1.png" width="310">
</p>

---

## 🔐 Verificación de autenticidad

<p align="center">
  <img src="/docs/pruebas/prototype/prototype2.png" width="310">
</p>

---

## 🌐 Exportación a plataforma externa

<p align="center">
  <img src="/docs/pruebas/adapter/adapter1.png" width="310">
</p>

⬆ [Volver al contenido](#contenido)

---

<a name="arquitectura"></a>

# 🏗 Arquitectura del Sistema

<p align="center">
  <img src="/docs/uml/uml_generalV2.png" width="510">
</p>

⬆ [Volver al contenido](#contenido)

---

<a name="patrones"></a>

# 🧩 Patrones de Diseño Implementados

## 📊 Resumen de Patrones

| Patrón | Tipo | Propósito | Aplicación |
|------|------|------|------|
| Prototype | Creacional | Clonación | Copias de obras |
| Adapter | Estructural | Adaptación | Exportación externa |

---

## Prototype

```
python
def clonar(self, nuevo_id):
    copia = deepcopy(self)
    copia.id = nuevo_id
    return copia
```

---

## Adapter

```
python
class adaptadorartesubasta:
    def exportar(self, obra):
        return {
            "description": obra.descripcion
        }
```

---

<a name="api"></a>

# 🔌 API Endpoints

| Método | Endpoint | Descripción |
|------|------|------|
| GET | /catalogo | Obtener catálogo |
| POST | /nuevo_producto_u_obra | Crear obra |
| POST | /clonar_obra_por/{id} | Clonar obra |
| POST | /generar_coleccion_masa/{id} | Generar copias |
| GET | /verificar_autenticidad/{id} | Validar obra |
| GET | /exportar_a_plataforma/{id} | Exportar obra |

⬆ [Volver al contenido](#contenido)

---

<a name="pruebas"></a>

# 🧪 Pruebas del Sistema

| Patrón | Evidencia |
|------|------|
| Singleton | [Visualizar](/docs/pruebas/singleton) |
| Factory | [Visualizar](/docs/pruebas/factory_method) |
| Builder | [Visualizar](/docs/pruebas/builder) |
| Prototype | [Visualizar](/docs/pruebas/prototype) |
| Adapter | [Visualizar](/docs/pruebas/adapter) |

⬆ [Volver al contenido](#contenido)

---

<a name="tecnologias"></a>

# 🛠 Tecnologías Utilizadas

| Tecnología | Uso |
|------|------|
| Python | Lenguaje |
| FastAPI | API |
| Swagger | Pruebas |
| UML | Diseño |
| GitHub | Versionamiento |

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
│   ├── uml/
│   ├── pruebas/
│   │   ├── singleton/
│   │   ├── factory_method/
│   │   ├── builder/
│   │   ├── prototype/
│   │   └── adapter/
```

⬆ [Volver al contenido](#contenido)

---

<a name="metodologia"></a>

# ⚙ Metodología

1. Análisis del problema  
2. Diseño UML  
3. Implementación FastAPI  
4. Integración de patrones  
5. Pruebas de endpoints  

⬆ [Volver al contenido](#contenido)

---

<a name="referencias"></a>

# 📚 Referencias

```
Sánchez, G. (2025). Patrones de diseño y estrategias reutilizables en la
automatización de pruebas de software.
```

⬆ [Volver al contenido](#contenido)

---

<a name="autores"></a>

# 👨‍💻 Autores

Jesús David Pérez Florian  
Andrés Felipe Florez Pérez

⬆ [Volver al contenido](#contenido)
