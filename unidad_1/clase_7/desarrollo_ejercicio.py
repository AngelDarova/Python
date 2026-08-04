def calcular_velocidad(distancia_km: float, tiempo_horas: float) -> float:
    """formula es distancia/tiempo """
    return distancia_km / tiempo_horas

def evaluar_multa(velocidad: float) -> bool:
    if velocidad > 120.0:
        return True
    else:
        return False
    
def mostrar_pantalla_radar(velocidad_final: float, genera_multa: bool):
    print("== PANEL DEL RADAR DE TRAFICO ==")
    print(f"Velocidad detectada: {velocidad_final:.1f} km/h")
    if genera_multa:
        print("🚨  MULTA GENERADA, infraccion")
    else:
        print("👍  Vehiculo dentro del rango premitido")
    print("===================================")
    
def operar_radar():
    print("--- INICIANDO CONTROL DEL TRAFICO ---")
    distancia = float(input("Ingrese los kilometros recorridos por el auto: "))
    tiempo = float(input("Ingrese las horas empleadas en el recorrido: "))
    
    #calcular la velocidad
    velocidad_auto = calcular_velocidad(distancia, tiempo)
    
    #evaluar si hay multa
    es_infractor = evaluar_multa(velocidad_auto)
    
    #mostrar pantalla radar
    mostrar_pantalla_radar(velocidad_auto, es_infractor)
    
operar_radar()