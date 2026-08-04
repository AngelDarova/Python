class aireAcondicionado:
    #constructor
    def __init__(self, marca, modelo, temp):
        self.marca = marca
        self.modelo = modelo
        self.__temp = 24
        
        #aqui validamos si temp esta entre 16 y 30, sino queda en 24
        if 16<=temp<=30:
            self.__temp = temp
        else:
            print("temperatura inicial invalida. Se asigno 24°C por defecto")
            
    #funciones para atributo protegido
    #getter            
    def get_temperatura(self):
        return self.__temp
    
    #setter
    def set_temperatura(self, nueva_tempepratura):
        if 16<=nueva_tempepratura<=30:
            self.__temp = nueva_tempepratura
            print("temperatura actualizada")
        else:
            print("Error: la temperatura debe estar entre 16 y 30°C")
    
    def aumentar_temp(self):
        if self.__temp<30:
            self.__temp += 1
        else:
            print("Temperatura maxima alcanzada")
            
    def disminuir_temp(self):
        if self.__temp>16:
            self.__temp -= 1
        else:
            print("Temperatura minima alcanzada")
            
    def consultar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Temperatura actual: {self.__temp}°C")

print("CREANDO AIRE ACONDICIONADO")
aire1 = aireAcondicionado("Samsung", "AT234", 18)
aire1.consultar_info()

aire1.disminuir_temp()
aire1.disminuir_temp()
aire1.disminuir_temp()
aire1.disminuir_temp()


aire1.consultar_info()