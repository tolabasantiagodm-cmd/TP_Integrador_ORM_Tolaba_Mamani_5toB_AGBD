#   Caso D - Pizzeria / Restaurante   /// Caso Elegido
#   Un local de comida necesita registrar sus productos, los pedidos, los clientes y los repartidores.
#   - Cliente (id, nombre, apellido, telefono, direccion)
#   - Producto (id, nombre, descripcion, precio, activo)
#   - Repartidor (id, nombre, apellido, activo)
#   - Pedido (id, fecha, total, estado, cliente_id, repartidor_id)

# git pull : rae tods los cambios del repositorio

from sqlalchemy imprt Col
from sqlalchemy.oorm import DeclarativeBase

class base(DeclarativeBase):
    pass

class Cliente(base):
    __tablename__ = "Clientes"

    id        = Column(Integer, primary_key=True)
    nombre    = Column(String)
    apellido = Column(String)
    telefono    = Column(In)
    direccion     = Column(Integer)

class Producto(base):
    __tablename__ = "Productos"

    id        = Column(Integer, primary_key=True)
    nombre    = Column(String)
    categoria = Column(String)
    precio    = Column(Float)
    stock     = Column(Integer)
    activo    = Column(Boolean, default=True)
