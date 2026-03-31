# ⚙ Backend

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

El backend del proyecto corresponde a la **API REST del sistema**, desarrollada con **FastAPI**.

Este módulo es responsable de gestionar toda la lógica del sistema, incluyendo:

- gestión de usuarios
- gestión de productos
- procesamiento de pedidos
- lógica del marketplace
- integración con servicios externos

---

# 🧩 Responsabilidades

El backend se encarga de:

- exponer endpoints REST
- manejar la lógica de negocio
- interactuar con la base de datos
- validar datos de entrada
- gestionar autenticación y autorización

---

# 🚀 Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- SQLAlchemy (o futuro ORM)
- PostgreSQL

---

# 🔌 Endpoints principales

Ejemplos de endpoints:

- GET /productos
- POST /productos
- GET /usuarios
- POST /pedidos

---

# ▶ Ejecución (próximamente)

``` 
bash
uvicorn main:app --reload
```

---

# 📂 Estructura esperada

```
backend/
│
├── main.py
├── models/
└── database/
```

---

📌 Este módulo representa el núcleo lógico del sistema.
