from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, asignaturas):
        for x in asignaturas:
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno):
        self.listadoAlumnos.append(alumno)

    @classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre