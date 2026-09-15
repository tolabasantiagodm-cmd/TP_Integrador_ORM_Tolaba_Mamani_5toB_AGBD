#   Caso D - Pizzeria / Restaurante   /// Caso Elegido
#   Un local de comida necesita registrar sus productos, los pedidos, los clientes y los repartidores.
#   - Cliente (id, nombre, apellido, telefono, direccion)
#   - Producto (id, nombre, descripcion, precio, activo)
#   - Repartidor (id, nombre, apellido, activo)
#   - Pedido (id, fecha, total, estado, cliente_id, repartidor_id)

# git pull : trae tods los cambios del repositorio

from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "Clientes"

    id        = Column(Integer, primary_key=True)
    nombre    = Column(String(50))
    apellido  = Column(String(50))
    telefono  = Column(String(20))
    direccion = Column(String)

class Producto(Base):
    __tablename__ = "Productos"

    id          = Column(Integer, primary_key=True)
    nombre      = Column(String)
    descripcion = Column(String)
    precio      = Column(Integer)
    activo      = Column(Boolean, default=True)

engine = create_engine("sqlite:///mi_tabla.db")
Base.metadata.create_all(engine)

Clientes_a_insertar = [
    Cliente(nombre="juan", apellido="gomez", telefono="1128745689", direccion="G.paz"),
    Cliente(nombre="juan", apellido="gomez", telefono="1128745689", direccion="G.paz"),
    Cliente(nombre="juan", apellido="gomez", telefono="1128745689", direccion="G.paz"),
    Cliente(nombre="juan", apellido="gomez", telefono="1128745689", direccion="G.paz"),
    Cliente(nombre="juan", apellido="gomez", telefono="1128745689", direccion="G.paz")
]

Productos_a_insertar = [
    Producto(nombre="joel", descripcion="descripcion del producto", precio=1000, activo=True),
    Producto(nombre="joel", descripcion="descripcion del producto", precio=1000, activo=True),
    Producto(nombre="joel", descripcion="descripcion del producto", precio=1000, activo=True),
    Producto(nombre="joel", descripcion="descripcion del producto", precio=1000, activo=True),
    Producto(nombre="joel", descripcion="descripcion del producto", precio=1000, activo=True)
]

with Session(engine) as session:
#    session.add_all(Clientes_a_insertar)
#    session.add_all(Productos_a_insertar)
#    session.commit()

#    total_productos = session.query(Producto).count()
#    print(f"total de los productos insertados : {total_productos}")

    filtro_productos = session.query(Producto).filter(Producto.precio > 900).all

    for p in filtro_productos:
        print(f"nombre del producto = {p.nombre}")
