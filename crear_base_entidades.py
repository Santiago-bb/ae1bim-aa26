from sqlalchemy import Column, Integer, String, ForeignKey
from configuracion import Base, engine

class Facultad(Base):
    __tablename__ = 'facultades'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String)
    decano = Column(String)

class Carrera(Base):
    __tablename__ = 'carreras'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo_interno = Column(String, unique=True)
    #Relación: Una carrera pertenece a una facultad
    facultad_id = Column(Integer, ForeignKey('facultades.id'))

class Profesor(Base):
    __tablename__ = 'profesores'
    id = Column(Integer, primary_key=True)
    nombres_apellidos = Column(String, nullable=False)
    correo = Column(String)
    especialidad = Column(String)
    #Relación: Un profesor pertenece a una carrera
    carrera_id = Column(Integer, ForeignKey('carreras.id'))

class RecursoAcademico(Base):
    __tablename__ = 'recursos_academicos'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    fecha_publicacion = Column(String)
    tipo = Column(String)
    url = Column(String)
    #Relación: Un recurso pertenece a un profesor
    profesor_id = Column(Integer, ForeignKey('profesores.id'))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("¡Base de datos y tablas creadas con éxito!")