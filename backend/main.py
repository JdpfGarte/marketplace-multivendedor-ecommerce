#python -m uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from models import (
    inventariosistema, fabricafisica, fabricadigital, 
    obrabuilder, adaptadorartesubasta,
    # nuevos import para el decorator
    NotificacionBasica, EmailDecorador, WhatsAppDecorador
)

from models import (
    inventariosistema, fabricafisica, fabricadigital, 
    obrabuilder, adaptadorartesubasta,
    NotificacionBasica, EmailDecorador, WhatsAppDecorador,
    # añade estos nuevos:
    formatopdf, formatoexcel, reporteinventario 
)

app = FastAPI()

# patron singleton gestiona los datos globales
inventario_global = inventariosistema()

@app.post("/nuevo_producto_u_obra")
def agregar_producto(
    id: int, nombre: str, artista: str, stock: int, precio: int, 
    tipo: str, extra: str, 
    certificado: bool = False, empaque: bool = False, seguro: int = 0
):
    # regla de integridad por el singleton
    if any(o.id == id for o in inventario_global.lista_obras):
        raise HTTPException(status_code=400, detail=f"el id {id} ya esta en uso. elige uno diferente.")

    # patron abstract factory segun el tipo de obra
    if tipo == "fisico":
        fabrica = fabricafisica()
    elif tipo == "digital":
        fabrica = fabricadigital()
    else:
        raise HTTPException(status_code=400, detail="tipo no valido")

    try:
        # patron factory method crea la instancia base de la obra
        nueva_obra_base = fabrica.crear(id, nombre, artista, stock, precio, extra)

        # patron builder configuracion paso a paso de atributos opcionales
        builder = obrabuilder(nueva_obra_base)
        builder.con_certificado(certificado).con_empaque(empaque)
        
        if seguro > 0:
            builder.con_seguro(seguro)
        
        obra_final = builder.construir()

        # persistencia mediante el singleton
        inventario_global.lista_obras.append(obra_final)
        inventario_global.guardar_datos() 
        
        # --- implementacion del patron decorator ---
        # iniciamos con la notificacion mas simple
        notificador = NotificacionBasica()

        # si la obra tiene certificado, decoramos con email
        if certificado:
            notificador = EmailDecorador(notificador)
        
        # si tiene seguro, decoramos tambien con whatsapp
        if seguro > 0:
            notificador = WhatsAppDecorador(notificador)

        # el mensaje final dependera de cuantas capas decoradores agregamos
        aviso_sistema = notificador.enviar(f"obra '{obra_final.obra}' registrada")

        return {
            "mensaje": "obra premium creada y guardada", 
            "notificacion_decorator": aviso_sistema,
            "obra": obra_final.__dict__
        }

    except ValueError as e:
        # captura validaciones builder
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/clonar_obra_por/{obra_id}")
def clonar_serie(obra_id: int, nuevo_id: int):
    # patron prototype buscamos el objeto original para ser clonado
    original = next((item for item in inventario_global.lista_obras if item.id == obra_id), None)
    if not original:
        raise HTTPException(status_code=404, detail="obra original no encontrada")
    
    # uso del metodo clonar definido en el patron prototipe
    nueva_copia = original.clonar(nuevo_id)
    inventario_global.lista_obras.append(nueva_copia)
    inventario_global.guardar_datos()
    
    return {"mensaje": f"copia edicion {nueva_copia.edicion} generada y guardada", "obra": nueva_copia.__dict__}

@app.get("/buscar_artista_por_su/{nombre}")
def buscar_obras(nombre: str):
    # busqueda integrado en el singleton
    resultados = inventario_global.buscar_por_artista(nombre)
    return {"encontradas": [o.__dict__ for o in resultados]}

@app.get("/catalogo_para_ver_todo")
def obtener_catalogo():
    # acceso a datos mediante singleton
    return {"galeria": [o.__dict__ for o in inventario_global.lista_obras]}

@app.get("/subastar/{obra_id}")
def subastar_obra(obra_id: int):
    obra_encontrada = next((item for item in inventario_global.lista_obras if item.id == obra_id), None)
    if not obra_encontrada:
        raise HTTPException(status_code=404, detail="obra no encontrada")
    
    # patron adapter: las obra interna para un servicio externo de subastas
    adaptador = adaptadorartesubasta(obra_encontrada)
    return {"resultado": adaptador.exportar_por_formato("uts")}

@app.delete("/eliminar_obra/{obra_id}")
def eliminar_obra(obra_id: int):
    # limpieza en el singleton
    obra_a_eliminar = next((item for item in inventario_global.lista_obras if item.id == obra_id), None)
    
    if not obra_a_eliminar:
        raise HTTPException(status_code=404, detail=f"no se encontro ninguna obra con el id {obra_id}")

    inventario_global.lista_obras.remove(obra_a_eliminar)
    inventario_global.guardar_datos()

    return {"mensaje": f"obra con id {obra_id} eliminada exitosamente"}

@app.get("/verificar_autenticidad/{obra_id}")
def verificar_obra(obra_id: int):
    # seguridad usando los metodos generados por el prototipe
    obra_encontrada = next((item for item in inventario_global.lista_obras if item.id == obra_id), None)
    
    if not obra_encontrada:
        raise HTTPException(status_code=404, detail="obra no registrada")

    tipo_de_obra = "original" if obra_encontrada.edicion == 1 else f"copia legal #{obra_encontrada.edicion}"
    
    return {
        "verificacion": "exitosa",
        "mensaje": f"esta es una {tipo_de_obra} de la obra '{obra_encontrada.obra}'",
        "codigo_seguridad_uts": obra_encontrada.sello
    }

@app.post("/generar_coleccion_masa/{obra_id}")
def generar_masa(obra_id: int, cantidad: int, id_inicio: int):
    # patron prototype generacion de multiples clones
    for i in range(id_inicio, id_inicio + cantidad):
        if any(o.id == i for o in inventario_global.lista_obras):
            raise HTTPException(status_code=400, detail=f"el id {i} ya esta ocupado")

    coleccion = inventario_global.generar_coleccion(obra_id, cantidad, id_inicio)
    if not coleccion:
        raise HTTPException(status_code=404, detail="obra base no encontrada")
    
    return {
        "mensaje": f"se han generado {cantidad} copias legales mediante prototype",
        "ejemplos": [c.__dict__ for c in coleccion[:2]]
    }

@app.get("/exportar_a_plataforma/{obra_id}")
def exportar_obra(obra_id: int, destino: str = "uts"):
    obra_encontrada = next((item for item in inventario_global.lista_obras if item.id == obra_id), None)
    if not obra_encontrada:
        raise HTTPException(status_code=404, detail="obra no encontrada")
    
    # patron adapter traduce la obra al formato especifico solicitado 
    adaptador = adaptadorartesubasta(obra_encontrada)
    resultado = adaptador.exportar_por_formato(destino)
    return {"plataforma_destino": destino, "respuesta_servidor": resultado}



@app.get("/generar_reporte_inventario/{formato_archivo}")
def obtener_reporte(formato_archivo: str):
    # elegimos la implementacion del puente (el formato)
    if formato_archivo.lower() == "pdf":
        implementacion = formatopdf()
    elif formato_archivo.lower() == "excel":
        implementacion = formatoexcel()
    else:
        raise HTTPException(status_code=400, detail="formato no soportado. usa 'pdf' o 'excel'")

    # creamos el reporte usando el brige
    mi_reporte = reporteinventario(implementacion)
    
    # procesamos los datos del singleton
    resultado = mi_reporte.crear_reporte(inventario_global.lista_obras)
    
    return {
        "patron_utilizado": "bridge",
        "descripcion": "separacion de tipo de reporte y formato de salida",
        "resultado": resultado
    }