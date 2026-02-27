# patron factory method para crear obras de arte
class obra:
    def __init__(self, id, obra, artista, stock, precio, categoria):
        self.id = id
        self.obra = obra
        self.artista = artista
        self.stock = stock
        self.precio = precio
        self.categoria = categoria

class fabricadearte:
    @staticmethod
    def crear_producto(id, obra, artista, stock, precio, categoria):
        # centraliza la creacion
        return obra(id, obra, artista, stock, precio, categoria)

# singleton para el inventario unico
class inventariosistema:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(inventariosistema, cls).__new__(cls)
            # datos iniciales del inventario
            cls._instancia.lista_obras = [
                {"id": 1, "obra": "atardecer al oleo", "artista": "andres florez", "stock": 5, "precio": 450000, "categoria": "pintura"},
                {"id": 2, "obra": "escultura de marmol", "artista": "jesus perez", "stock": 2, "precio": 890000, "categoria": "escultura"},
                {"id": 3, "obra": "cyberpunk 2077 art", "artista": "galeria multimarket", "stock": 10, "precio": 120000, "categoria": "digital"}
            ]
        return cls._instancia