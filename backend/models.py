# clase base
class obra:
    def __init__(self, id, nombre, artista, stock, precio, categoria):
        self.id = id
        self.obra = nombre
        self.artista = artista
        self.stock = stock
        self.precio = precio
        self.categoria = categoria

# familias nuevas
class obrafisica(obra):
    def __init__(self, id, nombre, artista, stock, precio, dimensiones):
        # llama a la base
        super().__init__(id, nombre, artista, stock, precio, "fisico")
        self.dimensiones = dimensiones

class obradigital(obra):
    def __init__(self, id, nombre, artista, stock, precio, formato):
        # llama a la base 
        super().__init__(id, nombre, artista, stock, precio, "digital")
        self.formato = formato

# fabricas especializadas
class fabricafisica:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obrafisica(id, nombre, artista, stock, precio, extra)

class fabricadigital:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obradigital(id, nombre, artista, stock, precio, extra)

# singleton: datos iniciales
class inventariosistema:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(inventariosistema, cls).__new__(cls)
            cls._instancia.lista_obras = [
                {"id": 1, "obra": "atardecer al oleo", "artista": "andres florez", "stock": 5, "precio": 450000, "categoria": "fisico"},
                {"id": 2, "obra": "escultura de marmol", "artista": "jesus perez", "stock": 2, "precio": 890000, "categoria": "fisico"},
                {"id": 3, "obra": "cyberpunk 2077 art", "artista": "galeria ", "stock": 10, "precio": 120000, "categoria": "digital"}
            ]
        return cls._instancia