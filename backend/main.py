from fastapi import FastAPI, HTTPException
from models import inventariosistema, fabricadearte # esto conecta los archivos

app = FastAPI()

# iniciamos el singleton
inventario_global = inventariosistema()
resenas_usuarios = []

@app.get("/catalogo")
def obtener_catalogo():
    return {"galeria": inventario_global.lista_obras}

@app.get("/recomendar/{obra_id}")
def recomendar_similares(obra_id: int):
    # buscamos en la lista del singleton para evitar el error de tu imagen
    obra_actual = next((item for item in inventario_global.lista_obras if item["id"] == obra_id), None)
    
    if not obra_actual:
        raise HTTPException(status_code=404, detail="obra no encontrada")
    
    recomendadas = [item for item in inventario_global.lista_obras if item["categoria"] == obra_actual["categoria"] and item["id"] != obra_id]
    
    return {
        "porque_te_gusto": obra_actual["obra"],
        "nuestra_ia_recomienda": recomendadas if recomendadas else "pronto mas obras aqui"
    }

@app.post("/calificar")
def calificar_obra(obra_id: int, estrellas: int, comentario: str):
    if estrellas < 1 or estrellas > 5:
        raise HTTPException(status_code=400, detail="calificacion de 1 a 5 solamente")
    
    nueva_resena = {"id_obra": obra_id, "puntos": estrellas, "comentario": comentario}
    resenas_usuarios.append(nueva_resena)
    return {"mensaje": "resena guardada", "resena": nueva_resena}

@app.get("/verificar/{producto_id}")
def verificar_stock(producto_id: int):
    for producto in inventario_global.lista_obras:
        if producto["id"] == producto_id:
            return {"disponible": producto["stock"] > 0, "cantidad": producto["stock"]}
    raise HTTPException(status_code=404, detail="no encontrado")

@app.post("/nuevo_producto")
def agregar_con_factory(id: int, nombre: str, artista: str, stock: int, precio: int, categoria: str):
    # uso de factory method
    nueva_obra_obj = fabricadearte.crear_producto(id, nombre, artista, stock, precio, categoria)
    # guardado en singleton
    inventario_global.lista_obras.append(nueva_obra_obj.__dict__)
    return {"mensaje": "obra creada con factory y guardada en singleton", "obra": nueva_obra_obj}