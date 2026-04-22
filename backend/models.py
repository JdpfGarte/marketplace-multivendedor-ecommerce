import copy
import json
import os
import uuid
from abc import ABC, abstractmethod

# --- PATRÓN COMPOSITE (Interfaz Base) ---
class ComponenteArte(ABC):
    @abstractmethod
    def obtener_precio(self) -> float:
        pass

    @abstractmethod
    def obtener_detalles(self) -> str:
        pass



# --- PATRÓN PROTOTYPE + COMPOSITE (Hoja) ---
class obra(ComponenteArte):
    def __init__(self, id, nombre, artista, stock, precio, categoria):
        self.id = id
        self.obra = nombre
        self.artista = artista
        self.stock = stock
        self.precio = precio
        self.categoria = categoria
        self.certificado = False
        self.empaque_regalo = False
        self.edicion = 1
        self.seguro = "sin seguro"
        self.sello = f"ORIGINAL-{uuid.uuid4().hex[:8].upper()}"

    def obtener_precio(self) -> float:
        # Si el seguro tiene un valor numérico lo sumaría, 
        # pero según tu lógica actual devuelve el precio base.
        return float(self.precio)

    def obtener_detalles(self) -> str:
        return f"{self.obra} ({self.artista}) - ${self.precio}"

    def clonar(self, nuevo_id):
        nueva_copia = copy.deepcopy(self)
        nueva_copia.id = nuevo_id
        nueva_copia.edicion += 1
        nueva_copia.sello = f"COPIA-LEGAL-{uuid.uuid4().hex[:8].upper()}"
        return nueva_copia

class obrafisica(obra):
    def __init__(self, id, nombre, artista, stock, precio, dimensiones):
        super().__init__(id, nombre, artista, stock, precio, "fisico")
        self.dimensiones = dimensiones

class obradigital(obra):
    def __init__(self, id, nombre, artista, stock, precio, formato):
        super().__init__(id, nombre, artista, stock, precio, "digital")
        self.formato = formato



# --- PATRÓN COMPOSITE (Contenedor) ---
class ColeccionArte(ComponenteArte):
    def __init__(self, id_coleccion, nombre_coleccion):
        self.id = id_coleccion
        self.nombre = nombre_coleccion
        self.componentes = []  # Lista que puede contener obras u otras colecciones
        self.categoria = "coleccion"
    def agregar(self, componente: ComponenteArte):
        self.componentes.append(componente)

    def eliminar(self, componente: ComponenteArte):
        self.componentes.remove(componente)

    def obtener_precio(self) -> float:
        #  suma recursivamente el precio de todo lo que contiene
        return sum(c.obtener_precio() for c in self.componentes)

    def obtener_detalles(self) -> str:
        detalles_internos = [c.obtener_detalles() for c in self.componentes]
        return f"COLECCIÓN: {self.nombre} | Items: {len(self.componentes)} | Contenido: [{', '.join(detalles_internos)}]"
    
    def contar_total_elementos(self) -> int:
        total = 0
        for c in self.componentes:
            if isinstance(c, ColeccionArte):
                total += c.contar_total_elementos() 
            else:
                total += 1 # Si es obra, cuenta 1
        return total



# --- PATRÓN BUILDER ---
class obrabuilder:
    def __init__(self, obra_instancia):
        self.obra = obra_instancia

    def con_certificado(self, tiene_certificado: bool):
        self.obra.certificado = tiene_certificado
        return self

    def con_empaque(self, tiene_empaque: bool):
        if tiene_empaque and self.obra.categoria == "digital":
            raise ValueError("error: las obras digitales no pueden tener empaque fisico.")
        self.obra.empaque_regalo = tiene_empaque
        return self
    
    def con_seguro(self, valor_asegurado: int):
        self.obra.seguro = f"asegurado por {valor_asegurado} usd"
        return self

    def construir(self):
        return self.obra



# --- PATRÓN ABSTRACT FACTORY ---
class fabricafisica:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obrafisica(id, nombre, artista, stock, precio, extra)

class fabricadigital:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obradigital(id, nombre, artista, stock, precio, extra)


# --- PATRÓN FLYWEIGHT (Compartir datos pesados) ---
class ContratoLegalFlyweight:
    """Estado Intrínseco: Datos que no cambian entre muchas obras"""
    def __init__(self, tipo_licencia: str, términos: str):
        self.tipo_licencia = tipo_licencia
        self.términos = términos

class FlyweightFactory:
    """Fábrica que gestiona la reutilización de objetos"""
    _licencias = {}

    @classmethod
    def obtener_licencia(cls, tipo_licencia: str):
        if tipo_licencia not in cls._licencias:
            print(f"FLYWEIGHT: Creando nueva licencia legal para '{tipo_licencia}'")
            # Simulamos un texto pesado que no queremos repetir en RAM
            terminos_pesados = f"Contrato estándar para {tipo_licencia}. Prohibida su reproducción total..."
            cls._licencias[tipo_licencia] = ContratoLegalFlyweight(tipo_licencia, terminos_pesados)
        else:
            print(f"FLYWEIGHT: Reutilizando licencia existente de '{tipo_licencia}'")
        
        return cls._licencias[tipo_licencia]



# --- PATRÓN SINGLETON ---
class inventariosistema:
    _instancia = None
    _archivo_datos = "inventario_arte.json"

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(inventariosistema, cls).__new__(cls)
            cls._instancia.lista_obras = []
            cls._instancia.cargar_datos()
        return cls._instancia
    
    def guardar_datos(self):
        with open(self._archivo_datos, "w") as f:
            # Usamos obtener_precio() 
            json.dump([o.__dict__ for o in self.lista_obras], f, indent=4, default=lambda x: str(x))

    def cargar_datos(self):
        if os.path.exists(self._archivo_datos):
            try:
                with open(self._archivo_datos, "r") as f:
                    datos = json.load(f)
                    self.lista_obras = [] # Limpiamos 
                    for d in datos:
                        # Si es una obra normal
                        if d.get('categoria') in ["fisico", "digital"]:
                            if d['categoria'] == "fisico":
                                obj = obrafisica(d['id'], d['obra'], d['artista'], d['stock'], d['precio'], d.get('dimensiones', ''))
                            else:
                                obj = obradigital(d['id'], d['obra'], d['artista'], d['stock'], d['precio'], d.get('formato', ''))
                            
                            obj.certificado = d.get('certificado', False)
                            obj.empaque_regalo = d.get('empaque_regalo', False)
                            obj.edicion = d.get('edicion', 1)
                            obj.seguro = d.get('seguro', "sin seguro")
                            obj.sello = d.get('sello', "S/N")
                            self.lista_obras.append(obj)
                        
                        # NUEVO: Si es una colección (Composite)
                        elif d.get('categoria') == "coleccion":
                            obj = ColeccionArte(d['id'], d.get('nombre', 'Coleccion Guardada'))
                            self.lista_obras.append(obj)
            except Exception as e:
                print(f"error al cargar datos: {e}")

    def generar_coleccion(self, obra_id, cantidad, id_inicio):
        original = next((o for o in self.lista_obras if o.id == obra_id), None)
        if not original: return None
        nuevas_copias = []
        for i in range(cantidad):
            copia = original.clonar(id_inicio + i)
            self.lista_obras.append(copia)
            nuevas_copias.append(copia)
        self.guardar_datos()
        return nuevas_copias

    def buscar_por_artista(self, artista_nombre):
        return [o for o in self.lista_obras if o.artista.lower() == artista_nombre.lower()]



# --- PATRÓN ADAPTER ---
class servicioexternonft:
    def enviar(self, metadata_json):
        return f"exito: datos exportados: {metadata_json}"

class adaptadorartesubasta:
    def __init__(self, obra_instancia):
        self.obra = obra_instancia
        self.servicio = servicioexternonft()

    def exportar_por_formato(self, destino: str):
        metadata = {
            "registro_institucional": self.obra.obra.upper(),
            "hash_verificacion": self.obra.sello,
            "tipo_bien": self.obra.categoria
        }
        return self.servicio.enviar(metadata)



# --- PATRÓN DECORATOR ---
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> str: pass

class NotificacionBasica(Notificacion):
    def enviar(self, mensaje: str) -> str:
        return f"SISTEMA: {mensaje}"

class NotificacionDecorador(Notificacion):
    def __init__(self, envoltorio: Notificacion):
        self._envoltorio = envoltorio
    def enviar(self, mensaje: str) -> str:
        return self._envoltorio.enviar(mensaje)

class EmailDecorador(NotificacionDecorador):
    def enviar(self, mensaje: str) -> str:
        return f"{super().enviar(mensaje)} | [EMAIL ENVIADO AL ARTISTA]"

class WhatsAppDecorador(NotificacionDecorador):
    def enviar(self, mensaje: str) -> str:
        return f"{super().enviar(mensaje)} | [WHATSAPP ENVIADO AL ADMIN]"




# --- PATRÓN BRIDGE ---
class formatointerface(ABC):
    @abstractmethod
    def generar(self, contenido: str) -> str: pass

class formatopdf(formatointerface):
    def generar(self, contenido: str) -> str:
        return f"archivo [reporte_uts.pdf] generado. contenido: {contenido}"

class formatoexcel(formatointerface):
    def generar(self, contenido: str) -> str:
        return f"archivo [reporte_uts.xlsx] generado. contenido: {contenido}"

class reporte(ABC):
    def __init__(self, formato: formatointerface):
        self.formato = formato
    @abstractmethod
    def crear_reporte(self, lista_obras: list) -> str: pass

class reporteinventario(reporte):
    def crear_reporte(self, lista_obras: list) -> str:
        total_obras = len(lista_obras)
        # Importante: usamos obtener_precio() por el Composite
        valor_total = sum(o.obtener_precio() for o in lista_obras)
        resumen = f"total de obras: {total_obras}, valor comercial: ${valor_total} usd"
        return self.formato.generar(resumen)




# --- PATRÓN FACADE (LA FACHADA MAESTRA) ---
class FachadaGaleria:
    def __init__(self, inventario_instancia):
        self.inventario = inventario_instancia

    def registro_premium_total(self, id, nombre, artista, precio, tipo, extra):
        # 1. ORQUESTACIÓN: Uso de Abstract Factory según el tipo (Físico/Digital)
        fabrica = fabricafisica() if tipo == "fisico" else fabricadigital()
        obra_base = fabrica.crear(id, nombre, artista, 1, precio, extra)

        # 2. INTELIGENCIA DE NEGOCIO: Decisiones automáticas del Builder
        builder = obrabuilder(obra_base)
        builder.con_certificado(True) # Regla: Toda obra por fachada es certificada
        
        # Regla: Si la obra es cara (>2000), el seguro es del 50%, si no, del 25%
        valor_seguro = precio // 2 if precio > 2000 else precio // 4
        builder.con_seguro(valor_seguro)
        
        # Regla: Solo poner empaque si es física (evita errores de lógica)
        if tipo == "fisico":
            builder.con_empaque(True)
            
        obra_final = builder.construir()

        # 3. PERSISTENCIA: Uso del Singleton para guardar en el inventario real
        self.inventario.lista_obras.append(obra_final)
        self.inventario.guardar_datos()

        # 4. ADAPTACIÓN AUTOMÁTICA: Si es digital, se envía a NFT usando el ADAPTER
        msj_nft = "No requiere NFT"
        if tipo == "digital":
            adaptador = adaptadorartesubasta(obra_final)
            msj_nft = adaptador.exportar_por_formato('OPENSEA-NFT-UTS')

        # 5. NOTIFICACIÓN DINÁMICA: Uso del DECORATOR según el precio
        notificador = NotificacionBasica()
        if precio > 1000:
            notificador = EmailDecorador(notificador)
        if precio > 5000:
            notificador = WhatsAppDecorador(notificador)
        
        estado_notificacion = notificador.enviar(f"Fachada: Obra Premium '{nombre}'")

        # 6. REPORTE AUTOMÁTICO: Uso del BRIDGE para generar comprobante
        # La fachada decide generar un PDF de confirmación automáticamente
        formato_pdf = formatopdf()
        bridge_reporte = reporteinventario(formato_pdf)
        comprobante = bridge_reporte.crear_reporte([obra_final])

        # Retornamos un diccionario organizado para que el Swagger se vea profesional
        return {
            "estado_notificaciones": estado_notificacion,
            "integracion_externa": msj_nft,
            "reporte_automatico": comprobante,
            "detalle_seguro": f"Seguro aplicado: ${valor_seguro} USD"
        }
    



    # --- PATRÓN PROXY El Intermediario de Seguridad ---
class ProxyFachada:
    def __init__(self, fachada_real: FachadaGaleria):
        self._fachada_real = fachada_real
        self._token_secreto = "UTSAD"

    def peticion_segura(self, token: str, id, nombre, artista, precio, tipo, extra):
        # 1. Control de Acceso (Verificación)
        if token != self._token_secreto:
            return {"error": "403 - Acceso Denegado", "detalle": "Token incorrecto"}
        
        # 2. Logging (Registro de quién entra)
        print(f"Proxy: Acceso autorizado para la obra '{nombre}'")
        
        # 3. Delegación (Llamar a la fachada real)
        return self._fachada_real.registro_premium_total(id, nombre, artista, precio, tipo, extra)