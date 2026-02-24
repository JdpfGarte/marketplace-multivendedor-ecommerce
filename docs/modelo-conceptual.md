# Modelo Conceptual

## Entidades Principales

### Usuario
- id
- nombre
- email
- password
- rol (comprador / vendedor / administrador)

### Producto
- id
- nombre
- descripcion
- precio
- stock
- vendedor_id

### Pedido
- id
- fecha
- total
- estado
- usuario_id

### Carrito
- id
- usuario_id

### Reseña
- id
- comentario
- calificacion
- producto_id
- usuario_id

### Pago
- id
- metodo
- estado
- pedido_id

### Recomendacion
- id
- usuario_id
- producto_id
