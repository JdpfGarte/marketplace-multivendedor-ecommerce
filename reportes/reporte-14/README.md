<div align="center">

# 📊 Reporte Semana 14  
### Marketplace Multivendedor Ecommerce

![Report](https://img.shields.io/badge/Report-Week%2014-blue)  
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

En la semana 14 se amplió el sistema mediante la implementación de dos patrones estructurales clave:

🔐 Proxy → Control de acceso seguro al sistema  
⚡ Flyweight → Optimización de memoria mediante reutilización de objetos  

El sistema evoluciona permitiendo:

🔐 Validación de acceso mediante token  
🛡 Protección de la Fachada real  
⚙ Delegación controlada de operaciones  
⚡ Reutilización de licencias legales  
📦 Reducción de objetos repetidos en memoria  

---

# 🎯 Objetivos del Proyecto

✔ Implementar Proxy  
✔ Controlar el acceso al sistema real  
✔ Validar solicitudes mediante token  
✔ Implementar Flyweight  
✔ Reutilizar objetos compartidos  
✔ Optimizar el consumo de memoria  

---

# 🎬 Demo del Sistema

## 🔐 Proxy

<p align="center">
  <img src="/docs/pruebas/proxy/proxy1.png" width="550">
</p>

## ⚡ Flyweight

<p align="center">
  <img src="/docs/pruebas/flyweight/flyweight1.png" width="550">
</p>

---

# 🧩 Patrones de Diseño Implementados

| Patrón | Tipo | Aplicación |
|------|------|------|
| Proxy | Estructural | Control de acceso |
| Flyweight | Estructural | Optimización de memoria |

---

## Proxy

```
python
resultado = proxy_seguro.peticion_segura(
    token, id, nombre, artista, precio, tipo, extra
)
```

---

## Flyweight

```
python
l1 = FlyweightFactory.obtener_licencia("Comercial")
l2 = FlyweightFactory.obtener_licencia("Comercial")
```

---

# 🔌 API Endpoints

| Método | Endpoint |
|------|------|
| POST | /registro_seguro_con_proxy |
| GET | /demo_optimizacion_flyweight |

---

# 🧪 Pruebas

✔ Proxy → Acceso denegado con token incorrecto  
✔ Proxy → Acceso exitoso con token válido  
✔ Flyweight → Reutilización de objetos en memoria  
✔ Flyweight → Validación de referencias compartidas  

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
├── proxy.py
├── flyweight.py
```

---

# ⚙ Metodología

1. Diseño UML  
2. Implementación del patrón Proxy  
3. Validación de acceso con token  
4. Implementación del patrón Flyweight  
5. Pruebas de reutilización de objetos  
6. Validación en Swagger  

---

# 👨‍💻 Autores

Jesús David Pérez Florian  
Andrés Felipe Florez Pérez  
