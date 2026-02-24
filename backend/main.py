from fastapi import FastAPI
from typing import List

app = FastAPI(title="MultiMarket - API de Arte y Diseño")

inventario_arte = [
    {
        "id": 1, 
        "obra": "Atardecer al Óleo", 
        "artista": "Andrés Flórez", 
        "stock": 5, 
        "precio": 450000,
        "categoria": "Pintura"
    },
    {
        "id": 2, 
        "obra": "Escultura de Mármol Moderna", 
        "artista": "Jesús Pérez", 
        "stock": 2, 
        "precio": 890000,
        "categoria": "Escultura"
    },
    {
        "id": 3, 
        "obra": "Ilustración Digital Cyberpunk", 
        "artista": "Galería MultiMarket", 
        "stock": 10, 
        "precio": 120000,
        "categoria": "Arte Digital"
    }
]

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al Marketplace de Arte MultiMarket"}

@app.get("/catalogo")
def obtener_catalogo():
    """Retorna todas las obras disponibles en el catálogo"""
    return {"productos": inventario_arte}

@app.get("/verificar/{producto_id}")
def verificar_disponibilidad(producto_id: int):
    """Verifica si una obra tiene stock (Inventario)"""
    for item in inventario_arte:
        if item["id"] == producto_id:
            estado = "Disponible" if item["stock"] > 0 else "Agotado"
            return {
                "obra": item["obra"],
                "stock_actual": item["stock"],
                "estado": estado
            }
    return {"error": "Obra no encontrada"}