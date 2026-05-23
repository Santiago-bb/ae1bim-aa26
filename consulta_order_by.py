from configuracion import session
from crear_base_entidades import Facultad

print("--- ORDENAMIENTO: FACULTADES ORDENADAS ALFABÉTICAMENTE ---")

#Ordenamos de forma ascendente por el campo nombre
facultades_ordenadas = session.query(Facultad).order_by(Facultad.nombre.asc()).all()

for f in facultades_ordenadas:
    print(f"Facultad: {f.nombre} | Ubicación: {f.ubicacion} | Decano: {f.decano}")