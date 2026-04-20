<div align="center">

# 📊 Reporte Semana 12  
### Marketplace Multivendedor Ecommerce

![Report](https://img.shields.io/badge/Report-Week%2012-blue)  
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

# 📘 Introducción

En la semana 12 se amplió el sistema mediante la implementación de dos patrones estructurales clave:

🧩 Facade → Simplificación del acceso al sistema  
🌳 Composite → Gestión jerárquica de colecciones  

El sistema evoluciona permitiendo:

🎨 Registro inteligente de obras  
⚙ Automatización de lógica  
🌳 Creación de colecciones  
📊 Cálculo automático de precios  

---

# 🎯 Objetivos del Proyecto

✔ Implementar Facade  
✔ Implementar Composite  
✔ Automatizar decisiones  
✔ Gestionar estructuras jerárquicas  

---

# 🎬 Demo del Sistema

## 🧩 Facade

<p align="center">
  <img src="/docs/pruebas/facade/facade1.png" width="550">
</p>

## 🌳 Composite

<p align="center">
  <img src="/docs/pruebas/composite/composite1.png" width="550">
</p>

---

# 🧩 Patrones de Diseño Implementados

| Patrón | Tipo | Aplicación |
|------|------|------|
| Facade | Estructural | Registro inteligente |
| Composite | Estructural | Colecciones |

---

## Facade

```
python
fachada.registro_premium_total(id, nombre, artista, precio, tipo, extra)
```

---

## Composite

```
python
coleccion.agregar(obra)
total = coleccion.obtener_precio()
```

---

# 🔌 API Endpoints

| Método | Endpoint |
|------|------|
| POST | /registro_facade_premium_rapido |
| POST | /crear_coleccion_artistica |
| GET | /catalogo |

---

# 🧪 Pruebas

✔ Facade → Flujo automático  
✔ Composite → Agrupación y suma  

---

# 🛠 Tecnologías

Python  
FastAPI  
Swagger  
UML  

---

# 📂 Estructura

```
marketplace/
├── main.py
├── facade.py
├── composite.py
```

---

# ⚙ Metodología

1. Diseño  
2. Implementación  
3. Pruebas  

---

# 👨‍💻 Autores

Jesús David Pérez Florian  
Andrés Felipe Florez Pérez  
