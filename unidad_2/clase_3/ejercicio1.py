class Estudiante:
    
    # constructor
    def __init__(self, nombre, curso, avance):
        self.nombre = nombre
        self.curso = curso
        self.__avance = 0
    #continuar este metodo con las validaciones    
        if 0<=avance<=100:
            self.__avance = avance
        else:
            print("El avance debe estar entre 0 y 100.")
            
    def get_avance(self):
        return self.__avance
    
    def completar_actividad(self,avance):
        if (0<=avance<=100):
            if (self.__avance+avance<=100):
                self.__avance += avance
            else:
                self.__avance = 100

        else:
            print("Error: avance debe estar entre 0 y 100.")
    
    def set_avance(self, nuevo_avance):
        if 0<=nuevo_avance<=100:
            self.__avance = nuevo_avance
            print("Avance actualizado correctamente")
        else:
            print("Error: el avance debe estar entre 0 y 100.")
        
    def mostrar_info(self):
        print("\n---------INFORMACION DEL ESTUDIANTE---------")
        print(f"Nombre: {self.nombre}")
        print(f"Curso: {self.curso}")
        print(f"Avance: {self.__avance}%")
        
est1 = Estudiante("Ana Lopez", "Python", 10)

est1.mostrar_info()

print("\nconsultando avance:")
print(est1.get_avance(), "%")
#avance_est1 = est1.get_avance()
#print(avance_est1, "%")

est1.completar_actividad(100)
print("\nconsultando avance:")
print(est1.get_avance(), "%")