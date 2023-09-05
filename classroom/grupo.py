from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", estudiantes=None, asignaturas=None):
        self._grupo = grupo
        self._asignaturas = asignaturas or []
        self.listadoAlumnos = estudiantes or []

    def listadoAsignaturas(self, *args):
        for x in args:
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre