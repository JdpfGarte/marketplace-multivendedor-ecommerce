# clase base con atributos comunes
class obra:
    def __init__(self, id, nombre, artista, stock, precio, categoria):
        self.id = id
        self.obra = nombre
        self.artista = artista
        self.stock = stock
        self.precio = precio
        self.categoria = categoria
# atributos opcionales para el builder
        self.certificado = False
        self.empaque_regalo = False

# especialidad fisica
class obrafisica(obra):
    def __init__(self, id, nombre, artista, stock, precio, dimensiones):
        super().__init__(id, nombre, artista, stock, precio, "fisico")
        self.dimensiones = dimensiones

# especialidad digital
class obradigital(obra):
    def __init__(self, id, nombre, artista, stock, precio, formato):
        super().__init__(id, nombre, artista, stock, precio, "digital")
        self.formato = formato

# clase builder para armar extras paso - paso
class obrabuilder:
    def __init__(self, obra_instancia):
        self.obra = obra_instancia

    def con_certificado(self, tiene_certificado: bool):
        self.obra.certificado = tiene_certificado
        return self

    def con_empaque(self, tiene_empaque: bool):
        self.obra.empaque_regalo = tiene_empaque
        return self

    def construir(self):
        return self.obra

# fabrica fisica abstract factory parte 1
class fabricafisica:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obrafisica(id, nombre, artista, stock, precio, extra)

# fabrica digital abstract factory parte 2
class fabricadigital:
    @staticmethod
    def crear(id, nombre, artista, stock, precio, extra):
        return obradigital(id, nombre, artista, stock, precio, extra)

# singleton para el inventario unico
class inventariosistema:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(inventariosistema, cls).__new__(cls)
            cls._instancia.lista_obras = []
        return cls._instancia