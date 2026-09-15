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

class Repartidor(Base):
    __tablename__ = "Repartidores"

    id        = Column(Integer, primary_key=True)
    nombre    = Column(String(50))
    apellido  = Column(String(50))
    activo = Column(Boolean, default=True)

class Pedido(Base):
    __tablename__ = "Pedidos"

    id        = Column(Integer, primary_key=True)
    fecha = Column(String)
    total    = Column(Integer)
    cliente_id  = Column(Integer)
    repartidor_id  = Column(Integer)

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

Repartidores_a_insertar = [
    Producto(nombre="jose",apellido="luis",activo=True),
    Producto(nombre="juan",apellido="borges",activo=True),
    Producto(nombre="julio",apellido="inturias",activo=True),
    Producto(nombre="pedro",apellido="alvarez",activo=True),
    Producto(nombre="beto",apellido="velez",activo=True)
]

Pedidos_a_insertar = [
    Producto(fecha=17092025,total=5000,cliente_id=12,repartidor_id=11),
    Producto(fecha=17092025,total=5000,cliente_id=34,repartidor_id=12),
    Producto(fecha=17092025,total=5000,cliente_id=23,repartidor_id=13),
    Producto(fecha=17092025,total=5000,cliente_id=14,repartidor_id=14),
    Producto(fecha=17092025,total=5000,cliente_id=24,repartidor_id=15)
]

with Session(engine) as session:
    session.add_all(Clientes_a_insertar)
    session.add_all(Productos_a_insertar)
    session.add_all(Repartidores_a_insertar)
    session.add_all(Pedidos_a_insertar)
    session.commit()

    total_clientes = session.query(Cliente).count()
    print(f"total de los clientes insertados : {total_clientes}")

    total_productos = session.query(Producto).count()
    print(f"total de los productos insertados : {total_productos}")

    total_repartidores = session.query(Repartidor).count()
    print(f"total de los repartidores insertados : {total_repartidores}")

    total_pedidos = session.query(Pedido).count()
    print(f"total de los pedidos insertados : {total_pedidos}")

#    filtro_productos = session.query(Producto).filter(Producto.precio > 900).all
#
#    for p in filtro_productos:
#        print(f"nombre del producto = {p.nombre}")
