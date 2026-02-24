from fastapi import FastAPI, HTTPException

app = FastAPI()

inventario_arte = [
    {"id": 1, "obra": "Atardecer al Óleo", "artista": "Andrés Flórez", "stock": 5, "precio": 450000, "categoria": "Pintura"},
    {"id": 2, "obra": "Escultura de Mármol", "artista": "Jesús Pérez", "stock": 2, "precio": 890000, "categoria": "Escultura"},
    {"id": 3, "obra": "Cyberpunk 2077 Art", "artista": "Galería MultiMarket", "stock": 10, "precio": 120000, "categoria": "Digital"}
]

#  Sistema de Reseñas 
resenas_usuarios = []

@app.post("/calificar")
def calificar_obra(obra_id: int, estrellas: int, comentario: str):
    """Permite a los usuarios calificar una obra de 1 a 5"""
    if estrellas < 1 or estrellas > 5:
        raise HTTPException(status_code=400, detail="La calificación debe ser entre 1 y 5")
    
    nueva_resena = {"id_obra": obra_id, "puntos": estrellas, "comentario": comentario}
    resenas_usuarios.append(nueva_resena)
    return {"mensaje": "Reseña guardada con éxito", "resena": nueva_resena}

# "IA" de Recomendación 
@app.get("/recomendar/{obra_id}")
def recomendar_similares(obra_id: int):
    """Simulación de ML: Recomienda obras de la misma categoría"""
    
    obra_actual = next((item for item in inventario_arte if item["id"] == obra_id), None)
    
    if not obra_actual:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    
    
    recomendadas = [item for item in inventario_arte if item["categoria"] == obra_actual["categoria"] and item["id"] != obra_id]
    
    return {
        "porque_te_gusto": obra_actual["obra"],
        "nuestra_ia_recomienda": recomendadas if recomendadas else "Pronto tendremos más obras de esta categoría"
    }


@app.get("/catalogo")
def obtener_catalogo():
    return {"galeria": inventario_arte}

@app.get("/verificar/{producto_id}")
def verificar_stock(producto_id: int):
    for producto in inventario_arte:
        if producto["id"] == producto_id:
            return {"disponible": producto["stock"] > 0, "cantidad": producto["stock"]}
    raise HTTPException(status_code=404, detail="Producto no encontrado")