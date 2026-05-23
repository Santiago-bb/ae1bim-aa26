from sqlalchemy import and_
from configuracion import session
from crear_base_entidades import RecursoAcademico

print("--- CONSULTA CON OPERADOR AND: FILTRADO DOBLE ---")

#Buscamos recursos que cumplan ambas condiciones estrictamente
recursos_filtrados = session.query(RecursoAcademico).filter(
    and_(
        RecursoAcademico.titulo == 'Guía de SQLAlchemy',
        RecursoAcademico.tipo == 'Guía de estudio'
    )
).all()

for r in recursos_filtrados:
    print(f"Encontrado -> Título: {r.titulo} | Tipo: {r.tipo} | URL: {r.url}")