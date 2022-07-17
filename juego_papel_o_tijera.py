import random

jugador1 = int(input("Ingrese '1' para jugar contra la maquina o '2' para jugar con otro jugador: "))
opciones = ("Papel","Tijera","Piedra")
puntos_jugador1 = 0
puntos_jugador2 = 0
puntos_maquina = 0

def maquina(opciones):
    return random.choice(opciones)

if jugador1 == 2:
    nombre_jugador2 = input("Ingrese un nombre Jugador2: ")
    print("------------------ Modo Multijugador ------------------\n")
elif jugador1 == 1:
    nombre_jugador1 = input("Ingrese su nombre Jugador1: ")
    print("------------------ Modo solitario ------------------\n")
else:
    print("Error ----------------------- Error\nLa opcion dijitada no es valida intenta de nuevo")
    
print("Ganas con dos puntos")

while (jugador1 == 1):
    print("---------------------------------------------------")
    if puntos_jugador1 == 2:
        print(f"\nGanaste {nombre_jugador1}")
        break
    elif puntos_maquina == 2: 
        print(f"\nLo siento {nombre_jugador1} perdiste")
        break
    
    opciones_jugador1 = input("\nIngrese una opcion 'Papel' , 'Tijera' , 'Piedra' ----> ")
    
    if opciones_jugador1 in opciones[0]:
        print(f"{nombre_jugador1} ----> 'Papel'")
        
        opcion_maquina = maquina(opciones)
        print(f"Maquina ----> {opcion_maquina}")
        
        if opcion_maquina == opciones[0]:
            print("Sin puntos")
        elif opcion_maquina == opciones[1]:
            print("Puntos para la maquina")
            puntos_maquina += 1
        elif opcion_maquina == opciones[2]:
            print(f"Puntos para {nombre_jugador1}")
            puntos_jugador1 += 1
            
    elif opciones_jugador1 in opciones[1]:
        print(f"{nombre_jugador1} ----> 'Tijera'")

        opcion_maquina = maquina(opciones)
        print(f"Maquina ----> {opcion_maquina}")
        
        if opcion_maquina == opciones[0]:
            print(f"Puntos para {nombre_jugador1}")
            puntos_jugador1 += 1
        elif opcion_maquina == opciones[1]:
            print("Sin puntos")
        elif opcion_maquina == opciones[2]:
            print("Puntos para la maquina")
            puntos_maquina += 1

    elif opciones_jugador1 in opciones[2]:
        print(f"{nombre_jugador1} ----> 'Piedra'")

        opcion_maquina = maquina(opciones)
        print(f"Maquina ----> {opcion_maquina}")
        
        if opcion_maquina == opciones[0]:
            print("puntos para la maquina")
            puntos_maquina += 1
        elif opcion_maquina == opciones[1]:
            print(f"Puntos para {nombre_jugador1}")
            puntos_jugador1 += 1
        elif opcion_maquina == opciones[2]:
            print("Sin puntos")
            
    else:
        print("Error ----------------------- Error\nLa opcion dijitada no es valida intenta de nuevo")
            
    print(f"\nPuntos {nombre_jugador1} ----> {puntos_jugador1} \nPuntos Maquina ----> {puntos_maquina}\n")
else:
    pass

while (jugador1 == 2):
    print("---------------------------------------------------")
    if puntos_jugador1 == 2:
        print(f"\nGanaste {nombre_jugador1}")
        break
    elif puntos_jugador2 == 2: 
        print(f"\nGanaste {nombre_jugador2} perdiste")
        break
    
    opciones_jugador1 = input(f"\nIngrese una opcion {nombre_jugador1}, 'Papel' , 'Tijera' , 'Piedra' ----> ")
    opciones_jugador2 = input(f"\nIngrese una opcion {nombre_jugador2}, 'Papel' , 'Tijera' , 'Piedra' ----> ")
    
    if opciones_jugador1 == opciones[0] and opciones_jugador2 == opciones[0]:
        print("Sin puntos")
    elif opciones_jugador1 == opciones[0] and opciones_jugador2 == opciones[1]:
        print(f"Puntos para {nombre_jugador2}")
        puntos_jugador2 += 1
    elif opciones_jugador1 == opciones[0] and opciones_jugador2 == opciones[2]:
        print(f"Puntos para {nombre_jugador1}")
        puntos_jugador1 += 1
    elif opciones_jugador1 == opciones[1] and opciones_jugador2 == opciones[0]:
        print(f"Puntos para {nombre_jugador1}")
        puntos_jugador1 += 1
    elif opciones_jugador1 == opciones[1] and opciones_jugador2 == opciones[1]:
        print("Sin puntos")
    elif opciones_jugador1 == opciones[1] and opciones_jugador2 == opciones[2]:
        print(f"Puntos para {nombre_jugador2}")
        puntos_jugador2 += 1
    elif opciones_jugador1 == opciones[2] and opciones_jugador2 == opciones[0]:
        print(f"Puntos para {nombre_jugador2}")
        puntos_jugador2 += 1
    elif opciones_jugador1 == opciones[2] and opciones_jugador2 == opciones[1]:
        print(f"Puntos para {nombre_jugador1}")
        puntos_jugador1 += 1
    elif opciones_jugador1 == opciones[2] and opciones_jugador2 == opciones[2]:
        print("Sin puntos")
    else:
        print("Error ----------------------- Error\nLa opcion dijitada no es valida intenta de nuevo")
        
    print(f"\nPuntos {nombre_jugador1} ----> {puntos_jugador1} \nPuntos {nombre_jugador2} ----> {puntos_jugador2}\n")
else:
    pass