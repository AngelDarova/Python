class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        
estudiantes = [
    {"nombre": "Juan", "edad": 20, "promedio": 4.2},
    {"nombre": "Gabriela", "edad": 20, "promedio": 8.6},
    {"nombre": "Mateo", "edad": 22, "promedio": 9.0},
    {"nombre": "Alejandro", "edad": 19, "promedio": 8.1},
    {"nombre": "Daniel", "edad": 21, "promedio": 9.2},
    {"nombre": "Natalia", "edad": 23, "promedio": 7.6},
]

def mostrar_estudiantes(lista):
    print("\n----------------------------------")
    print(f'{estudiante["Nombre"]: <15} {estudiante["Edad"]:<8} {estudiante[promedio]}')