# 🧠 Modelo Conceptual del Sistema

El modelo conceptual describe las **entidades principales del sistema y sus relaciones**, permitiendo comprender cómo se organiza la información dentro de la aplicación.

## 🎨 Entidad principal: Obra

La entidad central del sistema es **Obra**, que representa cualquier elemento artístico registrado en el inventario de la galería.

Cada obra contiene información como:

- identificador
- nombre
- artista
- precio
- stock disponible

## 🖼 Tipos de obra

El sistema maneja dos tipos principales de obras:

### Obras físicas

Representan piezas de arte tradicionales que existen en formato físico.

Ejemplos:

- pinturas
- esculturas
- ilustraciones

Estas obras pueden tener propiedades adicionales como:

- dimensiones
- tipo de material
- certificado de autenticidad

### Obras digitales

Representan arte en formato digital.

Ejemplos:

- arte digital
- ilustraciones digitales
- NFTs

Estas obras pueden incluir información como:

- formato del archivo
- resolución
- tipo de archivo

## 📦 Inventario

Todas las obras registradas se almacenan dentro de un **inventario centralizado**, que mantiene la lista completa de productos disponibles.

Este inventario se gestiona mediante el **patrón Singleton**, garantizando una única instancia dentro del sistema.
