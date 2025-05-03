"""
Simulador de Voley 
"""
import random

class Equipo:
    def __init__(self, nombre_equipo):
        self.nombre = nombre_equipo
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0 

equipo1 = Equipo("Alianza Lima")
equipo2 = Equipo("Regatas Lima")

def Puntos():
    puntos_set = random.randint(10, 28)
    return puntos_set

def PuntosExtras():
    extras = random.randint(0, 6)
    return extras

def RegistraSet(numero_equipo_ganador):
    
    global equipo1, equipo2
    partido_terminado = False 
    if numero_equipo_ganador == 1:
        equipo1.setGanados = equipo1.setGanados + 1
        if equipo1.setGanados == 3:
            print(f"  Set y Partido para {equipo1.nombre}") 
            equipo1.partidosGanados = equipo1.partidosGanados + 1 
            equipo2.partidosPerdidos = equipo2.partidosPerdidos + 1 
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            partido_terminado = True 
        else:
             print(f"  Set para {equipo1.nombre}. (Sets: {equipo1.setGanados}-{equipo2.setGanados})") 
             
    elif numero_equipo_ganador == 2:
        equipo2.setGanados = equipo2.setGanados + 1 
        if equipo2.setGanados == 3:
            print(f"  Set y Partido para {equipo2.nombre}") 
            equipo2.partidosGanados = equipo2.partidosGanados + 1 
            equipo1.partidosPerdidos = equipo1.partidosPerdidos + 1 
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            partido_terminado = True 
        else:
             print(f"  Set para {equipo2.nombre}. (Sets: {equipo1.setGanados}-{equipo2.setGanados})") 
             
    return partido_terminado

def JugarPartido():
   
    print("\n--- Comienza un nuevo Partido ---")
    sets_jugados = 0

    while True: 
        sets_jugados = sets_jugados + 1
        print(f"-> Jugando Set {sets_jugados}...")
        puntos_equipo1 = Puntos()
        puntos_equipo2 = Puntos()
        print(f"Puntos iniciales: {equipo1.nombre} {puntos_equipo1} - {puntos_equipo2} {equipo2.nombre}")

        while True: 
            ganador_del_set = 0 

            if puntos_equipo1 >= 25 and puntos_equipo1 > puntos_equipo2:
                ganador_del_set = 1 
            elif puntos_equipo2 >= 25 and puntos_equipo2 > puntos_equipo1:
                ganador_del_set = 2 
            if ganador_del_set != 0:
                break 
            else:
                print("Necesitan puntos extras...")
                puntos_equipo1 = puntos_equipo1 + PuntosExtras()
                puntos_equipo2 = puntos_equipo2 + PuntosExtras()
                print(f"Nuevos puntos: {equipo1.nombre} {puntos_equipo1} - {puntos_equipo2} {equipo2.nombre}")
                
        termino = RegistraSet(ganador_del_set)
        if termino == True:
            break 

def ResultadoTorneo():
    print("\n================================")
    print("   RESULTADOS DEL TORNEO ")
    print("================================")
    print(f"Equipo: {equipo1.nombre}")
    print(f"  Partidos Ganados: {equipo1.partidosGanados}")
    print(f"  Partidos Perdidos: {equipo1.partidosPerdidos}")
    print("--------------------------------")
    print(f"Equipo: {equipo2.nombre}")
    print(f"  Partidos Ganados: {equipo2.partidosGanados}")
    print(f"  Partidos Perdidos: {equipo2.partidosPerdidos}")
    print("================================")

if __name__ == "__main__":
    print("*********************************")
    print("  PARTIDO DE VOLEY  ")
    print("*********************************")
    while True: 
        try:
            texto_partidos = input("¿cuántos partidos quieres?: ")
            numero_de_partidos = int(texto_partidos) 
            if numero_de_partidos > 0:
                break 
            else:
                print("ingresa un número mayor a 0.")
        except ValueError:
            print("no es un número válido.")

    print(f"\nOk, simulando {numero_de_partidos} partidos...")
    for i in range(numero_de_partidos):
        JugarPartido()
    ResultadoTorneo()
    print("\nPartido Terminado")