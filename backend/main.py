from fastapi import FastAPI, HTTPException
from typing import List
# Importamos todo lo que construimos en el models
from models import (
    inventariosistema, fabricafisica, fabricadigital, obrabuilder,
    adaptadorartesubasta, reporteinventario, formatopdf, formatoexcel,
    ColeccionArte, FachadaGaleria
)

app = FastAPI(title="Galería de Arte UTS - Sistema Multifuncional")
sistema = inventariosistema()
fachada = FachadaGaleria(sistema)



# 1. PATRÓN ABSTRACT FACTORY + BUILDER
@app.post("/nuevo_producto_u_obra", tags=["Creacionales"])
def agregar_producto(id: int, nombre: str, artista: str, precio: int, tipo: str, extra: str):
    if any(o.id == id for o in sistema.lista_obras):
        raise HTTPException(status_code=400, detail="El ID ya existe")
    
    fabrica = fabricafisica() if tipo == "fisico" else fabricadigital()
    nueva_obra = fabrica.crear(id, nombre, artista, 1, precio, extra)
    
    # Builder para el seguro opcional
    builder = obrabuilder(nueva_obra)
    obra_final = builder.con_seguro(precio // 10).construir()
    
    sistema.lista_obras.append(obra_final)
    sistema.guardar_datos()
    return {"mensaje": "Obra creada con Factory y Builder", "obra": obra_final.obra}




# 2. PATRÓN PROTOTYPE (Clonación legal)
@app.post("/clonar_obra/{obra_id}", tags=["Creacionales"])
def clonar_obra(obra_id: int, nuevo_id: int):
    copias = sistema.generar_coleccion(obra_id, 1, nuevo_id)
    if not copias:
        raise HTTPException(status_code=404, detail="Obra original no encontrada")
    return {"mensaje": "Clon legal creado (Prototype)", "sello_nuevo": copias[0].sello}



# 3. PATRÓN COMPOSITE (Colecciones de obras)
@app.post("/crear_coleccion_artistica", tags=["Estructurales"])
def crear_coleccion(id_coleccion: int, nombre_coleccion: str, ids_obras: List[int]):
    if any(o.id == id_coleccion for o in sistema.lista_obras):
        raise HTTPException(status_code=400, detail="el id de la coleccion ya existe")
    
    nueva_coleccion = ColeccionArte(id_coleccion, nombre_coleccion)
    
    for oid in ids_obras:
        obra_obj = next((o for o in sistema.lista_obras if o.id == oid), None)
        if obra_obj:
            nueva_coleccion.agregar(obra_obj)
    
    if not nueva_coleccion.componentes:
        raise HTTPException(status_code=400, detail="debes incluir al menos una obra valida")

 
    sistema.lista_obras.append(nueva_coleccion) # La metemos a la lista global
    sistema.guardar_datos()                     
   
    
    return {
        "mensaje": "coleccion creada (patron composite)",
        "id_generado": id_coleccion,
        "precio_total": nueva_coleccion.obtener_precio(),
        "detalles": nueva_coleccion.obtener_detalles()
    }



# 4. PATRÓN ADAPTER (Exportar a Subastas/NFT)
@app.get("/exportar_subasta/{obra_id}", tags=["Estructurales"])
def exportar_obra(obra_id: int, destino: str = "OpenSea"):
    obra_obj = next((o for o in sistema.lista_obras if o.id == obra_id), None)
    if not obra_obj:
        raise HTTPException(status_code=404, detail="Obra no encontrada")
    
    adaptador = adaptadorartesubasta(obra_obj)
    return {"resultado": adaptador.exportar_por_formato(destino)}





# 5. PATRÓN BRIDGE (Reportes en PDF/Excel)
@app.get("/generar_reporte_inventario/{formato_archivo}", tags=["Estructurales"])
def obtener_reporte(formato_archivo: str):
    formato = formatopdf() if formato_archivo.lower() == "pdf" else formatoexcel()
    bridge_reporte = reporteinventario(formato)
    return {"descarga": bridge_reporte.crear_reporte(sistema.lista_obras)}




# 6. PATRÓN FACADE (Registro rápido Premium)
@app.post("/registro_facade_premium_rapido", tags=["Estructurales"])
def registro_facade(id: int, nombre: str, artista: str, precio: int, tipo: str, extra: str):
    resultado_notificacion = fachada.registro_premium_total(id, nombre, artista, precio, tipo, extra)
    return {"estado": "Procesado por Fachada", "notificaciones": resultado_notificacion}




# 7. MÉTODOS DE CONSULTA (Singleton)
@app.get("/catalogo_para_ver_todo", tags=["Sistema"])
def obtener_catalogo():
    return {"galeria": [o.__dict__ for o in sistema.lista_obras]}

@app.delete("/eliminar_obra/{obra_id}", tags=["Sistema"])
def eliminar_obra(obra_id: int):
    sistema.lista_obras = [o for o in sistema.lista_obras if o.id != obra_id]
    sistema.guardar_datos()
    return {"mensaje": f"Obra {obra_id} eliminada"}