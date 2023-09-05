from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinario", estudiantes=None, asignaturas=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    def listadoAsignaturas(self, *args):
        for arg in args:
            self._asignaturas.append(Asignatura(arg))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos += lista