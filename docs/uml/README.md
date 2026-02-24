Usuario
────────────────────────────
Atributos:
- id: int
- nombre: string
- email: string
- password: string
- rol: string

Métodos:
- registrar()
- login()

Descripción:
Representa a cualquier persona que interactúa con la plataforma (comprador, vendedor o administrador).
---
Producto
────────────────────────────
Atributos:
- id: int
- nombre: string
- descripcion: string
- precio: float
- stock: int

Métodos:
- actualizarStock()

Descripción:
Entidad que representa los artículos disponibles para la venta dentro del marketplace.
---
Pedido
────────────────────────────
Atributos:
- id: int
- fecha: date
- total: float
- estado: string

Métodos:
- calcularTotal()

Descripción:
Representa una transacción realizada por un comprador.
---
Carrito
────────────────────────────
Atributos:
- id: int

Métodos:
- agregarProducto()
- removerProducto()

Descripción:
Permite almacenar temporalmente productos antes de realizar la compra.
---
Reseña
────────────────────────────
Atributos:
- id: int
- comentario: string
- calificacion: int

Descripción:
Permite a los compradores calificar y comentar productos adquiridos.
---
Pago
────────────────────────────
Atributos:
- id: int
- metodo: string
- estado: string

Métodos:
- procesarPago()

Descripción:
Gestiona la información y el procesamiento del pago asociado a un pedido.
---
Recomendacion
────────────────────────────
Atributos:
- id: int
- puntaje: float

Descripción:
Representa el resultado del sistema de recomendaciones basado en comportamiento del usuario.
---
