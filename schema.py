#   Caso D - Pizzeria / Restaurante   /// Caso Elegido
#   Un local de comida necesita registrar sus productos, los pedidos, los clientes y los repartidores.
#   - Cliente (id, nombre, apellido, telefono, direccion)
#   - Producto (id, nombre, descripcion, precio, activo)
#   - Repartidor (id, nombre, apellido, activo)
#   - Pedido (id, fecha, total, estado, cliente_id, repartidor_id)

# git pull : rae tods los cambios del repositorio


from sqlalchemy import 
from sqlalchemy.orm import DeclarativeBase

class base(DeclarativeBase):
    pass

class Restaurante(base):
    __tablename__ = "Cliente"
    __tablename__ = "Producto"
    __tablename__ = "Repartidor"
    __tablename__ = "Pedido"