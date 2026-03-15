# 🧩 Pruebas del Patrón Singleton

![Singleton](https://img.shields.io/badge/Pattern-Singleton-purple)

El patrón **Singleton** garantiza que el sistema utilice **una única instancia
del inventario** durante toda la ejecución.

Esto permite que todas las operaciones trabajen sobre el mismo conjunto de datos.

---

# 🎯 Objetivo de la prueba

Verificar que el inventario del sistema:

- se cree una sola vez
- sea compartido por todas las operaciones
- mantenga la lista de obras registrada

---

# 📸 Evidencias

## Creación del inventario

![Creación inventario](singleton1.png)

---

## Registro de obras en el inventario

![Lista obras](singleton2.png)

---

# ✔ Resultado esperado

El sistema mantiene **una única instancia del inventario**, permitiendo que todas
las operaciones accedan al mismo almacenamiento de datos.
