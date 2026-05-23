from sqlalchemy import or_
from configuracion import session
from crear_base_entidades import RecursoAcademico

print("--- CONSULTA CON OPERADOR OR: FILTRADO FLEXIBLE ---")

#Buscamos recursos que cumplan una condición o la otra
recursos_flexibles = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == 'Guía de estudio',
        RecursoAcademico.titulo == 'Manual de Python'
    )
).all()

for r in recursos_flexibles:
    print(f"Encontrado -> Título: {r.titulo} | Tipo: {r.tipo}")