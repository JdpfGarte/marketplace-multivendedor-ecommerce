from fastapi import FastAPI, HTTPException
from models import inventariosistema, fabricafisica, fabricadigital

app = FastAPI()

# iniciamos el singleton
inventario_global = inventariosistema()
resenas_usuarios = []

@app.get("/catalogo")
def obtener_catalogo():
    return {"galeria": inventario_global.lista_obras}

@app.get("/recomendar/{obra_id}")
def recomendar_similares(obra_id: int):
    # busca en el singleton
    obra_actual = next((item for item in inventario_global.lista_obras if item["id"] == obra_id), None)
    
    if not obra_actual:
        raise HTTPException(status_code=404, detail="obra no encontrada")
    
    # recomienda fisico o digital
    recomendadas = [item for item in inventario_global.lista_obras if item["categoria"] == obra_actual["categoria"] and item["id"] != obra_id]
    
    return {
        "porque_te_gusto": obra_actual["obra"],
        "nuestra_ia_recomienda": recomendadas if recomendadas else "pronto mas obras aqui"
    }

@app.post("/nuevo_producto")
def agregar_con_abstract_factory(id: int, nombre: str, artista: str, stock: int, precio: int, tipo: str, extra: str):
    #decide que fabrica usar
    if tipo == "fisico":
        fabrica = fabricafisica()
        nueva_obra_obj = fabrica.crear(id, nombre, artista, stock, precio, extra)
    elif tipo == "digital":
        fabrica = fabricadigital()
        nueva_obra_obj = fabrica.crear(id, nombre, artista, stock, precio, extra)
    else:
        raise HTTPException(status_code=400, detail="tipo no valido. usa 'fisico' o 'digital'")

    # guardar en el singleton
    inventario_global.lista_obras.append(nueva_obra_obj.__dict__)
    
    return {
        "mensaje": f"obra {tipo} creada con abstract factory y guardada en singleton",
        "obra": nueva_obra_obj
    }