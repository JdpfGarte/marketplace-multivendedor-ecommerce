from fastapi import FastAPI, HTTPException
from models import inventariosistema, fabricafisica, fabricadigital, obrabuilder

app = FastAPI()

# iniciamos el singleton (Patron 1)
inventario_global = inventariosistema()

@app.get("/catalogo")
def obtener_catalogo():
    return {"galeria": inventario_global.lista_obras}

@app.get("/recomendar/{obra_id}")
def recomendar_similares(obra_id: int):
    obra_actual = next((item for item in inventario_global.lista_obras if item["id"] == obra_id), None)
    
    if not obra_actual:
        raise HTTPException(status_code=404, detail="obra no encontrada")
    
    recomendadas = [item for item in inventario_global.lista_obras if item["categoria"] == obra_actual["categoria"] and item["id"] != obra_id]
    
    return {
        "porque_te_gusto": obra_actual["obra"],
        "nuestra_ia_recomienda": recomendadas if recomendadas else "pronto mas obras aqui"
    }

@app.post("/nuevo_producto")
def agregar_producto(
    id: int, nombre: str, artista: str, stock: int, precio: int, 
    tipo: str, extra: str, 
    certificado: bool = False, empaque: bool = False # parametros para el builder
):
    # 1. decide fabrica Abstract Factory - Patron 2 y 3
    if tipo == "fisico":
        fabrica = fabricafisica()
    elif tipo == "digital":
        fabrica = fabricadigital()
    else:
        raise HTTPException(status_code=400, detail="tipo no valido")

    # 2. crea la base  Factory Method
    nueva_obra_base = fabrica.crear(id, nombre, artista, stock, precio, extra)

    # 3. aplica extras paso a paso (Builder - Patron 4)
    builder = obrabuilder(nueva_obra_base)
    if certificado:
        builder.con_certificado(True)
    if empaque:
        builder.con_empaque(True)
    
    obra_final = builder.construir()

    # 4. guardar en el singleton Patron 1
    inventario_global.lista_obras.append(obra_final.__dict__)
    
    return {
        "mensaje": "obra creada con los 4 patrones",
        "obra": obra_final
    }