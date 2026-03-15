# 📚 Documentación del Proyecto

![Docs](https://img.shields.io/badge/Documentation-Project-blue)
![UML](https://img.shields.io/badge/UML-Diagrams-orange)

Este directorio contiene **toda la documentación técnica y visual del sistema**.

Aquí se almacenan los recursos utilizados para explicar la arquitectura,
funcionamiento y estructura del proyecto.

---

## 📚 Documentación

| Documento | Descripción |
|----------|-------------|
| 📐 [Arquitectura](arquitectura.md) | Estructura general del sistema |
| 🧠 [Modelo conceptual](modelo-conceptual.md) | Representación de entidades del sistema |
| 📋 [Requerimientos](requerimientos.md) | Requerimientos funcionales y no funcionales |
| 🌍 [Roadmap](roadmap.md) | Plan de desarrollo y evolución del proyecto |

---

# 📁 Contenido

## 📐 UML

La carpeta `uml` contiene los **diagramas UML del sistema**, los cuales representan la arquitectura
y la implementación de los **patrones de diseño utilizados en el proyecto**.

Entre ellos:

- Diagrama general del sistema
- Diagrama del patrón **Singleton**
- Diagrama del patrón **Factory Method**
- Diagrama del patrón **Abstract Factory**
- Diagrama del patrón **Builder**

Estos diagramas permiten visualizar **cómo se relacionan las clases y componentes del sistema**.

```
docs/uml/
```
---

## 🧪 Pruebas

La carpeta **pruebas** contiene las **evidencias de funcionamiento del sistema** y demuestra la correcta implementación de los **patrones de diseño utilizados en el proyecto**.

Las pruebas consisten en capturas obtenidas durante la ejecución del sistema (generalmente desde **Swagger**), donde se observa el comportamiento de cada patrón aplicado.

En lugar de agrupar todas las capturas en un solo lugar, las pruebas se organizan **por patrón de diseño**, lo que permite analizar cada implementación de manera independiente.

---

### 📁 Organización de las pruebas

```
docs/pruebas/
│
├── singleton/
├── factory_method/
├── abstract_factory/
└── builder/
```

Cada carpeta contiene:

- capturas de ejecución del sistema
- explicación del comportamiento del patrón
- análisis técnico de los resultados obtenidos

---

### 🧩 Pruebas incluidas

| Patrón | Evidencia |
|-------|-----------|
| 🧩 Singleton | [Ver pruebas](pruebas/singleton/) |
| 🏭 Factory Method | [Ver pruebas](pruebas/factory_method/) |
| 🏭 Abstract Factory | [Ver pruebas](pruebas/abstract_factory/) |
| 🧱 Builder | [Ver pruebas](pruebas/builder/) |

Estas evidencias permiten visualizar cómo **cada patrón de diseño influye en el comportamiento del sistema** y cómo se aplican en la creación y configuración de las obras dentro del inventario.

---

📌 Esta carpeta sirve como **soporte visual para la documentación del proyecto y su explicación técnica**.
