# 📚 Documentación del Proyecto

![Docs](https://img.shields.io/badge/Documentation-Project-blue)
![UML](https://img.shields.io/badge/UML-Diagrams-orange)

Este directorio contiene **toda la documentación técnica y visual del sistema**.

Aquí se almacenan los recursos utilizados para explicar la arquitectura,
funcionamiento, evolución e implementación de los **patrones de diseño** del proyecto.

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
- Diagrama del patrón **Prototype**
- Diagrama del patrón **Adapter**
- Diagrama del patrón **Bridge**
- Diagrama del patrón **Decorator**

Estos diagramas permiten visualizar **la relación entre clases, componentes y patrones de diseño**, facilitando la comprensión del sistema.

---

## 🧪 Pruebas

La carpeta **pruebas** contiene las **evidencias de funcionamiento del sistema**, demostrando la correcta implementación de los patrones de diseño.

Las pruebas se basan en capturas obtenidas durante la ejecución del sistema (principalmente desde **Swagger**), donde se observa el comportamiento real de cada patrón.

Para mejorar la organización, las pruebas están estructuradas **por patrón de diseño**, permitiendo analizar cada uno de forma independiente.

---

### 📁 Organización de las pruebas

```
docs/pruebas/
│
├── singleton/
├── factory_method/
├── abstract_factory/
├── builder/
├── prototype/
├── adapter/
├── bridge/
└── decorator/
```

Cada carpeta contiene:

- capturas de ejecución del sistema  
- explicación del comportamiento del patrón  
- análisis técnico de los resultados obtenidos  

---

📌 Esta carpeta sirve como **soporte visual para la documentación del proyecto y su explicación técnica**.
