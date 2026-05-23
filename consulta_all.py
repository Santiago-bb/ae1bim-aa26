from configuracion import session
from crear_base_entidades import Profesor, Carrera

print("--- REPORTE GLOBAL: TODOS LOS PROFESORES Y SUS CARRERAS ---")

#Realizamos la consulta uniendo la tabla profesor con carrera
profesores = session.query(Profesor).join(Carrera).all()

for p in profesores:
    #Como están relacionadas accedemos a la carrera directamente
    carrera_asociada = session.query(Carrera).filter(Carrera.id == p.carrera_id).first()
    nombre_carrera = carrera_asociada.nombre if carrera_asociada else "Sin Carrera"
    
    print(f"Profesor: {p.nombres_apellidos} | Especialidad: {p.especialidad} | Carrera: {nombre_carrera}")