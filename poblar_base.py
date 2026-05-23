from configuracion import session
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

#Creamos una facultad de ejemplo
facu_sistemas = Facultad(nombre="Facultad de Sistemas", ubicacion="Bloque 4", decano="Ing. Juan Pérez")
session.add(facu_sistemas)
session.commit() #Guardamos para que genere un ID

#Creamos una carrera asociada a esa facultad
carrera_it = Carrera(nombre="Tecnologías de la Información", codigo_interno="TI-001", facultad_id=facu_sistemas.id)
session.add(carrera_it)
session.commit()

#Creamos un profesor asociado a la carrera
profe_alberto = Profesor(nombres_apellidos= "Alberto Avila", correo="alberto@utpl.edu.ec", especialidad="Desarrollo Web", carrera_id=carrera_it.id)
session.add(profe_alberto)
session.commit()

#Creamos un recurso asociado al profesor
recurso_guia = RecursoAcademico(titulo="Guía de SQLAlchemy", fecha_publicacion="2026-05-22", tipo="Guía de estudio", url="http://ejemplo.com/guia", profesor_id=profe_alberto.id)
session.add(recurso_guia)
session.commit()

print("¡Datos de prueba insertados correctamente!")