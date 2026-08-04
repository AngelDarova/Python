class Usuario:
    """representa la ficha individual de una persona en la biblioteca"""
    def __init__(self, cedula, nombre, correo, tipo):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.tipo = tipo #Estudiante, profesor, investigador
        
    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo
        
    def __repr__(self):
        return f"Usuario: {self.nombre} | Cédula: {self.cedula} | Correo {self.correo} | Tipo: {self.tipo}"
    
class SistemaUsuarios:
    """
    Administra la coleccion central de usuarios.
    Utilizaremos un diccionario como estructura principal donde:
    - Clave: cedula
    - Valor: Instancia de la clase usuario
    """
    
    def __init__(self):
        self.usuarios: dict[str, Usuario] = {}
        
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un nuevo usuario si su cedula no esta repetida"""
        if usuario.cedula in self.usuarios: #traduccion: si ya hay una llave con esa misma cedula
            print(f"Error, La cédula {usuario.cedula} ya se encuentra registrada")
            return False
        
        self.usuarios[usuario.cedula] = usuario #registrando el usuario nuevo
        print(f"{usuario.nombre} registrado exitosamente")
        return True
    def consultar_usuario(self, cedula: str) -> Usuario | None:
        if cedula in self.usuarios:
            return self.usuarios[cedula] #retorna el valor de la llave usuario
        print(f"El usuario con cédula {cedula} no fue encontrado")
        return None
    
    def actualizar_usuario(sefl, cedula: str):
        pass
    
    def eliminar_usuario(self, cedula: str):
        if cedula in self.usuarios:
            usuario_eliminado = self.usuarios.pop(cedula)
            print(f"usuario {usuario_eliminado.nombre} dado de baja exitosamente")
            return True
        
        print(f"No se pudo eliminar: la cedula {cedula} no esta registrada")
        return False