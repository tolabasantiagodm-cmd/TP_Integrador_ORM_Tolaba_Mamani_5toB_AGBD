from sqlalchemy.orm import Session, DeclarativeBase 
# Para eso traemos DeclarativeBase: la plantilla base del sistema ORM
from sqlalchemy import Column, Integer, String, Boolean, create_engine

class Base(DeclarativeBase): 
    # Creamos nuestra clase base; cualquiera que herede de ella 
    # será leída por SQLAlchemy como una tabla de datos.
    pass                     

class Producto(Base): 
    # Definimos nuestra tabla de productos aplicando la herencia
    __tablename__ = 'productos' 

    # Column es el constructor que avisa a SQLAlchemy que es un campo de la tabla
    id = Column(Integer, primary_key=True)
    # primary_key=True: Marca la columna id como la clave única y autoincremental en SQLite.
    
    nombre = Column(String) 
    # String le dice a la base de datos que guarde texto.
    
    precio = Column(Integer) 
    # CORREGIDO: Cambiamos Boolean por Integer para que soporte precios numéricos como 8500.
    
    stock = Column(Integer) 
    # Integer le dice a la base de datos que guarde números enteros para el inventario.

# CREAR EL ARCHIVO FISICO DE LA BASE DE DATOS Y LA CONEXION FISICA
engine = create_engine("sqlite:///mi_app.db")
# "create_engine" se encarga de conectarse a la base de datos.
# "sqlite:///mi_app.db" le indica que use SQLite y cree un archivo llamado mi_app.db.

# Creamos las tablas en la base de datos física
Base.metadata.create_all(engine)

# Definimos los productos que vamos a insertar
Productos_a_insertar = (
    Producto(id=1, nombre="Teclado mecanico", precio=8500, stock=15),
    Producto(id=2, nombre="Mouse inalambrico", precio=4200, stock=30)
)

# INTERACTUAR CON LA BASE DE DATOS (GUARDAR Y CONSULTAR)
# El "with" es un administrador: abre la sesión, realiza las operaciones 
# y cierra la conexión automáticamente al terminar para que el archivo no quede bloqueado.
with Session(engine) as session:
    # Agregamos los productos y guardamos los cambios (commit)
    session.add_all(Productos_a_insertar)
    session.commit()

    # CORREGIDO: Para consultar y recorrer los datos, usamos session.query()
    productos_guardados = session.query(Producto).all()

    for p in productos_guardados: 
        # Recorremos cada objeto (producto individual) devuelto por la consulta
        print(f"El nombre del producto es: {p.nombre} y su precio es ${p.precio}") 
        # Usamos la variable 'p' del bucle para imprimir las propiedades del registro actual.