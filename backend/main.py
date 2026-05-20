from fastapi import FastAPI, HTTPException
# ... después de fachada = FachadaGaleria(sistema)

from models import (
    inventariosistema, fabricafisica, fabricadigital, obrabuilder,
    adaptadorartesubasta, reporteinventario, formatopdf, formatoexcel,
    ColeccionArte, FachadaGaleria, ProxyFachada ,FlyweightFactory,PagoPasarelaEstandar, 
    PagoTransferenciaDirecta, PagoCriptoNFT,ColeccionistaSeguidor, AdministradorPlataforma,
     GestorNotificacionesObra,ComandoComprarObra
)
from typing import List
# Importamos todo lo que construimos en el models


app = FastAPI(title="Galería de Arte UTS - Sistema Multifuncional")
sistema = inventariosistema()
fachada = FachadaGaleria(sistema)
proxy_seguro = ProxyFachada(fachada)

# --- El nuevo Endpoint del Proxy ---
@app.post("/registro_protegido_proxy", tags=["Estructurales"])
def registro_proxy(token: str, id: int, nombre: str, artista: str, precio: int, tipo: str, extra: str):
    # El cliente ahora le pide al Proxy, no a la Fachada
    resultado = proxy_seguro.peticion_segura(token, id, nombre, artista, precio, tipo, extra)
    
    if "error" in resultado:
        raise HTTPException(status_code=403, detail=resultado["error"])
    
    return resultado



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


# 8. PATRÓN PROXY Acceso controlado a la Fachada
@app.post("/registro_seguro_con_proxy", tags=["Estructurales"])
def registro_con_proxy(token: str, id: int, nombre: str, artista: str, precio: int, tipo: str, extra: str):
    # Usa peticion_segura que es como lo defininos en el models
    resultado = proxy_seguro.peticion_segura(token, id, nombre, artista, precio, tipo, extra)
    
    if isinstance(resultado, dict) and "error" in resultado:
        raise HTTPException(status_code=403, detail=resultado["error"])
        
    return resultado




# 9. PATRÓN FLYWEIGHT (Ahorro de memoria)
@app.get("/demo_optimizacion_flyweight", tags=["Estructurales"])
def demo_flyweight():
    # Pedimos la misma licencia varias veces
    l1 = FlyweightFactory.obtener_licencia("Comercial")
    l2 = FlyweightFactory.obtener_licencia("Comercial") # Aquí se reutiliza
    l3 = FlyweightFactory.obtener_licencia("Educativa")
    
    return {
        "mensaje": "Demostración de Flyweight",
        "objetos_en_memoria": {
            "licencia_1_id": id(l1),
            "licencia_2_id": id(l2),
            "resultado": "Es el mismo objeto" if l1 is l2 else "Son diferentes"
        },
        "nota": "Fíjate en la consola de Python; verás que solo se 'creó' una vez la comercial."
    }


# 10. PATRÓN STATE (Simular la compra y cambio de comportamiento)
@app.post("/gestionar_ciclo_vida_state/{obra_id}", tags=["Comportamiento"])
def comprar_o_descontar_obra_patron_state(obra_id: int, accion: str = "comprar", descuento_porcentaje: float = 10.0):
    obra_obj = next((o for o in sistema.lista_obras if o.id == obra_id), None)
    if not obra_obj:
        raise HTTPException(status_code=404, detail="Obra no encontrada en el catálogo")
    
    # Comprobamos qué acción quiere ejecutar el cliente en el Marketplace
    if accion.lower() == "comprar":
        resultado = obra_obj.comprar_obra()
    elif accion.lower() == "descuento":
        resultado = obra_obj.rebajar_precio(descuento_porcentaje)
    else:
        raise HTTPException(status_code=400, detail="Acción no válida. Usa 'comprar' o 'descuento'")
    
    sistema.guardar_datos() # Persistimos el nuevo estado con el Singleton
    
    return {
        "obra": obra_obj.obra,
        "artista": obra_obj.artista,
        "precio_actual": obra_obj.precio,
        "stock_restante": obra_obj.stock,
        "estado_en_sistema": str(obra_obj.estado_actual.__class__.__name__),
        "resultado_operacion": resultado
    }



# 11. PATRÓN STRATEGY (Calcular totales de pago dinámicamente 
@app.get("/calcular_pago_strategy/{obra_id}", tags=["Comportamiento"])
def calcular_pago_obra_patron_strategy(obra_id: int, metodo_pago: str = "pasarela"):
    obra_obj = next((o for o in sistema.lista_obras if o.id == obra_id), None)
    if not obra_obj:
        raise HTTPException(status_code=404, detail="Obra no encontrada")

    # Selección dinámica de la estrategia
    if metodo_pago.lower() == "pasarela":
        estrategia = PagoPasarelaEstandar()
    elif metodo_pago.lower() == "transferencia":
        estrategia = PagoTransferenciaDirecta()
    elif metodo_pago.lower() == "cripto":
        estrategia = PagoCriptoNFT()
    else:
        raise HTTPException(status_code=400, detail="Método de pago no soportado. Usa 'pasarela', 'transferencia' o 'cripto'")

    # Extraemos el precio convirtiéndolo a flotante de forma segura
    precio_base = float(obra_obj.precio)

    # Ejecutamos el algoritmo de la estrategia elegida
    liquidacion = estrategia.calcular_total(precio_base)

    return {
        "obra_id": obra_obj.id,
        "titulo_obra": getattr(obra_obj, 'obra', 'Sin título'),
        "artista": getattr(obra_obj, 'artista', 'Anónimo'),
        "liquidacion_detallada": liquidacion
    }




# 14. PATRÓN OBSERVER (Notificar cambios de la obra a seguidores)
@app.post("/simular_notificacion_observer/{obra_id}", tags=["Comportamiento"])
def simular_alerta_obra_patron_observer(obra_id: int, evento: str = "cambio_precio"):
    obra_obj = next((o for o in sistema.lista_obras if o.id == obra_id), None)
    if not obra_obj:
        raise HTTPException(status_code=404, detail="Obra no encontrada")

    # Creamos el canal del sujeto (Observer)
    canal = GestorNotificacionesObra()

    # Suscribimos dinámicamente a los interesados
    cliente_vip = ColeccionistaSeguidor("Carlos_Bucaramanga")
    admin_sistema = AdministradorPlataforma()

    canal.suscribir(cliente_vip)
    canal.suscribir(admin_sistema)

    # Redactamos el mensaje según lo que pasó en el Marketplace
    if evento == "cambio_precio":
        mensaje = f"La obra '{obra_obj.obra}' cambió su precio comercial a ${obra_obj.precio} USD."
    elif evento == "vendida":
        mensaje = f"¡URGENTE! La pieza única '{obra_obj.obra}' ha sido vendida. Retirar de vitrinas."
    else:
        mensaje = f"Nueva actualización en la obra '{obra_obj.obra}'."

    # El sujeto le avisa a todos de golpe
    alertas_enviadas = canal.notificar_todos(mensaje)

    return {
        "obra_monitoreada": obra_obj.obra,
        "evento_ocurrido": evento,
        "cantidad_notificados": len(alertas_enviadas),
        "registro_de_alertas": alertas_enviadas
    }


# Variable global temporal para pruebas del Rollback
ultimo_comando_ejecutado = {}

# 15. PATRÓN COMMAND (Ejecutar compra encapsulada)
@app.post("/procesar_compra_command/{obra_id}", tags=["Comportamiento"])
def comprar_con_comando(obra_id: int):
    global ultimo_comando_ejecutado
    
    # Encapsulamos la petición en un objeto comando
    comando = ComandoComprarObra(sistema, obra_id)
    resultado = comando.ejecutar()
    
    if "Error" in resultado:
        raise HTTPException(status_code=400, detail=resultado)
        
    # Guardamos el objeto comando en memoria para poder revertirlo si se requiere
    ultimo_comando_ejecutado[obra_id] = comando
    sistema.guardar_datos()
    
    return {
        "transaccion": "Comando Recibido",
        "resultado_ejecucion": resultado,
        "ayuda": "Si simulas un fallo en el pago, puedes llamar al endpoint de deshacer."
    }

# 16. PATRÓN COMMAND (Deshacer / Rollback de la compra)
@app.post("/deshacer_compra_command/{obra_id}", tags=["Comportamiento"])
def deshacer_con_comando(obra_id: int):
    global ultimo_comando_ejecutado
    
    comando = ultimo_comando_ejecutado.get(obra_id)
    if not comando:
        raise HTTPException(status_code=400, detail="No hay una transacción reciente que se pueda revertir para este ID.")
        
    # Llamamos al método deshacer del objeto guardado
    resultado_rollback = comando.deshacer()
    
    # Limpiamos el historial de esa obra
    del ultimo_comando_ejecutado[obra_id]
    sistema.guardar_datos()
    
    return {
        "transaccion": "Rollback Exitoso",
        "detalle_sistema": resultado_rollback
    }