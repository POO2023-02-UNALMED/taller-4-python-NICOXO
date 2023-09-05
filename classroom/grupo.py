from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    def listadoAsignaturas(self, *asignaturas):
        for asignatura in asignaturas:
            self._asignaturas.append(Asignatura(asignatura))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre