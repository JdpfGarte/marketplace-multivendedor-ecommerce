import copy
import json
import os
import uuid

# patron prototype clase base con protocolo de autenticidad
class obra:
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
        #identificar el original
        self.sello = f"ORIGINAL-{uuid.uuid4().hex[:8].upper()}"

    def clonar(self, nuevo_id):
        # patron prototipe para copias
        nueva_copia = copy.deepcopy(self)
        nueva_copia.id = nuevo_id
        nueva_copia.edicion += 1
        # cada clon legal
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

# patron builder construccion paso a paso con reglas 
class obrabuilder:
    def __init__(self, obra_instancia):
        self.obra = obra_instancia

    def con_certificado(self, tiene_certificado: bool):
        self.obra.certificado = tiene_certificado
        return self

    def con_empaque(self, tiene_empaque: bool):
        # validacion de regla  del builder
        if tiene_empaque and self.obra.categoria == "digital":
            raise ValueError("error: las obras digitales no pueden tener empaque fisico.")
        self.obra.empaque_regalo = tiene_empaque
        return self
    
    def con_seguro(self, valor_asegurado: int):
        self.obra.seguro = f"asegurado por {valor_asegurado} usd"
        return self

    def construir(self):
        return self.obra

# patron abstract factory fabricas para familias de objetos
class fabricafisica:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obrafisica(id, nombre, artista, stock, precio, extra)

class fabricadigital:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obradigital(id, nombre, artista, stock, precio, extra)

# patron singleton instancia unica con persistencia y gestion de colecciones
class inventariosistema:
    _instancia = None
    _archivo_datos = "inventario_arte.json"

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(inventariosistema, cls).__new__(cls)
            cls._instancia.lista_obras = []
            cls._instancia.cargar_datos() # carga automatica al iniciar
        return cls._instancia
    
    def guardar_datos(self):
        # persiste los datos en un archivo json
        with open(self._archivo_datos, "w") as f:
            json.dump([o.__dict__ for o in self.lista_obras], f, indent=4)

    def cargar_datos(self):
        # recupera los datos guardados al reiniciar el sistema
        if os.path.exists(self._archivo_datos):
            try:
                with open(self._archivo_datos, "r") as f:
                    datos = json.load(f)
                    for d in datos:
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
            except Exception as e:
                print(f"error al cargar datos: {e}")

    #prototype para generar colecciones en masa
    def generar_coleccion(self, obra_id, cantidad, id_inicio):
        original = next((o for o in self.lista_obras if o.id == obra_id), None)
        if not original:
            return None
        
        nuevas_copias = []
        for i in range(cantidad):
            # clona n veces usando el metodo del prototype
            copia = original.clonar(id_inicio + i)
            self.lista_obras.append(copia)
            nuevas_copias.append(copia)
        
        self.guardar_datos()
        return nuevas_copias

    def buscar_por_artista(self, artista_nombre):
        return [o for o in self.lista_obras if o.artista.lower() == artista_nombre.lower()]

# patron adapter adaptacion de datos para servicios externos
class servicioexternonft:
    def enviar(self, metadata_json):
        return f"exito: datos exportados: {metadata_json}"

class adaptadorartesubasta:
    def __init__(self, obra_instancia):
        self.obra = obra_instancia
        self.servicio = servicioexternonft()

    def exportar_por_formato(self, destino: str):
        # traduce el objeto interno a formatos externos 
        if destino.lower() == "opensea":
            metadata = {
                "name": self.obra.obra,
                "description": f"art piece by {self.obra.artista}",
                "edition": self.obra.edicion,
                "external_url": f"https://uts.art/verify/{self.obra.sello}"
            }
        else:
            # formato uts
            metadata = {
                "registro_institucional": self.obra.obra.upper(),
                "autor_uts": self.obra.artista.upper(),
                "hash_verificacion": self.obra.sello,
                "tipo_bien": self.obra.categoria
            }
        return self.servicio.enviar(metadata)
    
    # -nuevo decorator ---
from abc import ABC, abstractmethod

# Interfaz notificaciones
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> str:
        pass

# notificación más básica
class NotificacionBasica(Notificacion):
    def enviar(self, mensaje: str) -> str:
        return f"SISTEMA: {mensaje}"

# base
class NotificacionDecorador(Notificacion):
    def __init__(self, envoltorio: Notificacion):
        self._envoltorio = envoltorio

    def enviar(self, mensaje: str) -> str:
        return self._envoltorio.enviar(mensaje)

# 1: Email
class EmailDecorador(NotificacionDecorador):
    def enviar(self, mensaje: str) -> str:
        resultado = super().enviar(mensaje)
        return f"{resultado} | [EMAIL ENVIADO AL ARTISTA]"

#2: WhatsApp
class WhatsAppDecorador(NotificacionDecorador):
    def enviar(self, mensaje: str) -> str:
        resultado = super().enviar(mensaje)
        return f"{resultado} | [WHATSAPP ENVIADO AL ADMIN]"
    



    # -nuevo bridge -
from abc import ABC, abstractmethod

# implementacion: define como se genera el archivo
class formatointerface(ABC):
    @abstractmethod
    def generar(self, contenido: str) -> str:
        pass

class formatopdf(formatointerface):
    def generar(self, contenido: str) -> str:
        return f"archivo [reporte_uts.pdf] generado con éxito. contenido: {contenido}"

class formatoexcel(formatointerface):
    def generar(self, contenido: str) -> str:
        return f"archivo [reporte_uts.xlsx] generado con éxito. contenido: {contenido}"

# define que informacion lleva el reporte
class reporte(ABC):
    def __init__(self, formato: formatointerface):
        # puente unimos el reporte con un formato
        self.formato = formato

    @abstractmethod
    def crear_reporte(self, lista_obras: list) -> str:
        pass

class reporteinventario(reporte):
    def crear_reporte(self, lista_obras: list) -> str:
        # logica para resumir el inventario
        total_obras = len(lista_obras)
        valor_total = sum(o.precio for o in lista_obras)
        resumen = f"total de obras: {total_obras}, valor comercial: ${valor_total} usd"
        # el puente envia los datos al formato elegido (pdf o excel)
        return self.formato.generar(resumen)