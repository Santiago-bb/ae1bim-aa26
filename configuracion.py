from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Motor de conexión a SQLite
engine = create_engine('sqlite:///universidad.db', echo=True)

#Sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()