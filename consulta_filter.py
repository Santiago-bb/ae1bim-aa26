from configuracion import session
from crear_base_entidades import RecursoAcademico

print("--- FILTRADO: RECURSOS DE TIPO 'Guía de estudio' ---")

#Filtramos usando el método filter
recursos_guias = session.query(RecursoAcademico).filter(RecursoAcademico.tipo == 'Guía de estudio').all()

for recurso in recursos_guias:
    print(f"Título: {recurso.titulo} | Tipo: {recurso.tipo} | URL: {recurso.url}")