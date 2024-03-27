import random
import time
import winsound
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

print ("Demostración de batalla por texto")
print ("Creado por FlexedGnu")
print("")

# Entrada de nombre

while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre != "":
        break

# Iniciador del sonido (pygame)

pygame.mixer.init()

sound = pygame.mixer.Sound("music.wav")

sound.play(loops=-1)

# Inicio del juego

print("")
print ("¡Te atacan!")

print ("ENEMIGO: Kshlotockhthomas")
time.sleep(1)

# Establecimiento de la vida del enemigo y el jugador

pvenemigo = 8000
pv = 6000

print("")
print ("Comandos: atacar, defender, cura, analisis, stats, ayuda")

# Declaración de algunas variables

defender = "Te has defendido, recibirás menos daño en el siguiente turno."
defense = ""
defensa = 0
cura = "Te has curado. Aumentas +",pv + random.randint(500,650), "tus HP."
debilidad = 200
atk = random.randint(800,1000)
defe = 0
atkene = random.randint(800,1000)
estado = "Limpio"
huboaccion1 = 0
finpartida = 0
debil = 0
magenemigo = "El enemigo usa magia. Tu siguiente ataque perderá fuerza."
magrest = 2
cant_cura = 10
debdef = 0
atkfuerte = 0
magfuerte = 0
huboenemigo = 0
atkeneplus = 0
habi_cool = 0

# Bucle 1: Maneja los turnos.
    # Se encarga de repetir los bucles de turnos para el jugador y el enemigo, verificar los efectos de estado y terminar la partida.

while True:
    
    # Bucle 2: Maneja el turno del jugador.
        # Aquí se encuentran todos los comandos que el jugador puede hacer.
    
    while True :
        winsound.PlaySound("tuturno.wav", winsound.SND_ASYNC)
        print("")
        accion1 = input("Acción: ")
        print("")
    
        if accion1 == "atacar":
            huboaccion1 = 1
            winsound.PlaySound("ataque.wav", winsound.SND_ASYNC)
            print ("Has atacado. Haces ", atk, " ATK.")
            pvenemigo = (pvenemigo - atk)
            defensa = 0
            time.sleep(1)
            
        
        elif accion1 == "defender":
            huboaccion1 = 1
            winsound.PlaySound("defender.wav", winsound.SND_ASYNC)
            print(defender)
            defense = "Defendiendo"
            defensa = 1
            time.sleep(1)
            
    
        elif accion1 == "cura":
            if cant_cura > 0:
                huboaccion1 = 1
                winsound.PlaySound("cura.wav", winsound.SND_ASYNC)
                cant_cura = cant_cura - 1
               
                pv = (pv + random.randint(500,650))
                
                if pv > 6000:
                    pv = 6000
                print ("Te has curado. Tienes", pv,"HP. Te quedan", cant_cura, "curas.")                
                defensa = 0
                time.sleep(1)
                
            else:
                print ("¡No te quedan curas!")
        
        elif accion1 == "analisis":
            print("Kshlotockhthomas, ", pvenemigo, " PV")
    
        elif accion1 == "stats":
            print(nombre, ": HP: ", pv, ", ATK: ", atk, ", Estado: ", estado, defense)
    
        elif accion1 == "ayuda":
            print("Explicación de los comandos:")
            print("")
            print("Atacar: Daña al oponente.")
            print("Defender: Reduce el daño del siguiente ataque.")
            print("Cura: Aumenta tus HP.")
            print("Análisis: Muestra la vida del oponente.")
            print("Stats: Muestra tus estadísticas.")
            print("Ayuda: Muestra esta lista.")
                    
        elif accion1 == "comandos":
            print ("Comandos: atacar, defender, cura, analisis, stats, ayuda")
        
        elif accion1 == "madeby":
            print ("01101010 01101101 01101010 01101000 01101111 01101110")
        
        elif accion1 == "za warudo":
            print("ZA WARUDO! TOKI WO TOMARE!!")
            winsound.PlaySound("zawarudo.wav", winsound.SND_ASYNC)
            time.sleep(1.5)
            winsound.PlaySound("tokiwo.wav", winsound.SND_ASYNC)
            sound.stop()
            sound = pygame.mixer.Sound("timestop.wav")
            sound.play()
            time.sleep(2)
            print("RODORORA DA!!!!")
            winsound.PlaySound("roadroller.wav", winsound.SND_ASYNC)
            time.sleep(1.5)
            winsound.PlaySound("diohaha.wav", winsound.SND_ASYNC)
            time.sleep(1.5)
            print("MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA MUDA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            winsound.PlaySound("mudamuda.wav", winsound.SND_ASYNC)
            time.sleep(2.3)
            print("MUDA!")
            winsound.PlaySound("muda.wav", winsound.SND_ASYNC)
            time.sleep(0.7)
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            time.sleep(2.5)
            print("Soshite toki wa ugokidasu.")
            winsound.PlaySound("soshite.wav", winsound.SND_ASYNC)
            time.sleep(3)
            pvenemigo = (pvenemigo - 10000)
            winsound.PlaySound("finaldio.wav", winsound.SND_ASYNC)
            huboaccion1 = 1
        
        # Acciones debug: Para hacer pruebas.
        
        elif accion1 == "debug_pv":
            print("Acción debug: Vida aumentada.")
            pv = 1000000

        elif accion1 == "debug_exit":
            print("Acción debug: Saliendo...")
            time.sleep(1)
            exit()

        elif accion1 == "debug_enepv":
            print("Acción debug: Vida del enemigo aumentada.")
            pvenemigo = 1000000

        # Verificador de acción
        
        if huboaccion1 == 1:
            break
            
    # Bucle 3: Se encarga de manejar el turno del enemigo.
        # Aquí se encuentran todas las acciones que el enemigo puede hacer.
        # Todo está manejado por números aleatorios, por lo que no hay una inteligencia artificial establecida, por ahora.
    
    while True and pvenemigo > 0 and pv > 0:
        if atkfuerte == 1:
            pv = (pv - 2500 + defe - atkeneplus) 
            debil = 0
            if pv > 0:
                print ("Te han atacado. Tienes ", pv," HP.")
            winsound.PlaySound("atkfuerte.wav", winsound.SND_ASYNC)
            atkfuerte = 0
            debil = 0
            accenemigo = random.randint(1, 6)
            habi_cool = habi_cool - 1
            huboenemigo = 1
            time.sleep(1)
        
        elif magfuerte == 1:
            print ("¿Cara o cruz?")
            while True:
                moneleg = input("Elección: ")
                if moneleg == "cara" or moneleg == "cruz":
                    break
                
            moneda = random.randint (1, 2)
            winsound.PlaySound("coin.wav", winsound.SND_ASYNC)
            print("...")
            time.sleep(2)
            if moneda == 1:
                print ("Cara.")
                if moneleg == "cara":
                    print("Esquivaste su ataque por los pelos.")
                    winsound.PlaySound("esquivar.wav", winsound.SND_ASYNC)
                    time.sleep(1)
                    debdef = 0
                    atkeneplus = 0
                    debil = 0
                    accenemigo = random.randint(1, 6)
                    magfuerte = 0
                    habi_cool = habi_cool - 1
                    huboenemigo = 1
                else:
                    pv = (pv - 4000 + defe - atkeneplus)
                    if pv > 0:
                        print ("Te han atacado. Tienes ", pv," HP.")
                    winsound.PlaySound("magfuerte.wav", winsound.SND_ASYNC)
                    time.sleep(1)
                    debdef = 0
                    atkeneplus = 0
                    debil = 0
                    accenemigo = random.randint(1, 6)
                    magfuerte = 0
                    habi_cool = habi_cool - 1
                    huboenemigo = 1
            else:
                print ("Cruz.")
                if moneleg == "cruz":
                    print("Esquivaste su ataque por los pelos.")
                    winsound.PlaySound("esquivar.wav", winsound.SND_ASYNC)
                    time.sleep(1)
                    debdef = 0
                    atkeneplus = 0
                    debil = 0
                    accenemigo = random.randint(1, 6)
                    magfuerte = 0
                    habi_cool = habi_cool - 1
                    huboenemigo = 1
                else:
                    pv = (pv - 4000 + defe - atkeneplus)
                    if pv > 0:
                        print ("Te han atacado. Tienes ", pv," HP.")
                    winsound.PlaySound("magfuerte.wav", winsound.SND_ASYNC)
                    time.sleep(1)
                    debdef = 0
                    atkeneplus = 0
                    debil = 0
                    accenemigo = random.randint(1, 6)
                    magfuerte = 0
                    habi_cool = habi_cool - 1
                    huboenemigo = 1
                
            
        elif huboenemigo == 0:
            accenemigo = random.randint(1, 6)
    
        if accenemigo == 1 and huboenemigo == 0:
            pv = (pv - atkene + defe - atkeneplus)
            debil = 0
            if pv > 0:
                print ("Te han atacado. Tienes ", pv," HP.")
            winsound.PlaySound("daño.wav", winsound.SND_ASYNC)
            time.sleep(1)
            debdef = 0
            atkeneplus = 0
            debil = 0
            habi_cool = habi_cool - 1
            huboenemigo = 1
            
            
        elif accenemigo == 2 and huboenemigo == 0 and habi_cool < 3:
            print (magenemigo)
            winsound.PlaySound("magatk.wav", winsound.SND_ASYNC)
            time.sleep(1)
            debil = 1
            debdef = 0
            habi_cool = habi_cool + 1
            huboenemigo = 1
            
        elif accenemigo == 3 and atkfuerte == 0 and huboenemigo == 0:
            print ("El enemigo prepara un ataque fuerte.")
            winsound.PlaySound("preparando.wav", winsound.SND_ASYNC)
            time.sleep(2)
            atkfuerte = 1
            debdef = 0
            debil = 0
            habi_cool = habi_cool - 1
            huboenemigo = 1
            
            
        elif accenemigo == 4 and magrest >= 2 and huboenemigo == 0:
            print ("El enemigo prepara un ataque mágico poderoso.")
            winsound.PlaySound("preparando.wav", winsound.SND_ASYNC)
            time.sleep(2)
            magfuerte = 1
            magrest = magrest - 1
            debdef = 0
            debil = 0
            habi_cool = habi_cool - 1
            huboenemigo = 1
            


        elif accenemigo == 5 and huboenemigo == 0 and habi_cool < 3:
            print ("El enemigo usa magia, tu defensa ha disminuido por el siguiente turno.")
            winsound.PlaySound("magdef.wav", winsound.SND_ASYNC)
            time.sleep(2)
            debdef = -200
            debil = 0
            habi_cool = habi_cool + 1
            huboenemigo = 1
            

        elif accenemigo == 6 and huboenemigo == 0 and habi_cool < 3:
            print ("El enemigo potencia su siguiente ataque.")
            winsound.PlaySound("atkplus.wav", winsound.SND_ASYNC)
            time.sleep(1)
            atkeneplus = 400
            debdef = 0
            debil = 0
            habi_cool = habi_cool + 1
            huboenemigo = 1
            
        # Verificador de accion del enemigo
            
        if huboenemigo == 1:
            break
            
    # Verificación de algunos datos, como los efectos de estado y si la partida debe terminar.

    if debil == 1:
        atk = (atk - debilidad)
        estado = "Débil"
    
    if debil == 0:
        atk = random.randint(800,1000)
        estado = "Limpio"

    if defensa == 1:
        defe = 200 - debdef
        defense = " (Defendiendo)"
    
    if defensa == 0:
        defe = 0 - debdef
        defense = ""

    if pvenemigo <= 0:
        print("Enemigo -Kshlotockhthomas- eliminado.")
        winsound.PlaySound("eliminado.wav", winsound.SND_ASYNC)
        time.sleep(1)
        sound.stop()
        print("")
        print("¡Has Ganado!")
        winsound.PlaySound("fanfare.wav", winsound.SND_ASYNC)
        time.sleep(4)
        print("")
        print("Gracias por jugar.")
        time.sleep(1)
        print("")
        finalizador = input("Presiona enter para salir...")
        if finalizador == "" or finalizador != "":
            finpartida = 1
    
    if pv <= 0 and pvenemigo > 0:
        sound.stop()
        time.sleep(1)
        print("")
        print("Has perdido...")
        winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)
        time.sleep(4)
        print("")
        print("Gracias por jugar.")
        time.sleep(2)
        print("")
        finalizador = input("Presiona enter para salir...")
        if finalizador == "" or finalizador != "":
            finpartida = 1
            
    # Reiniciador: Al reiniciar estas variables, si la condición posterior no se cumple, pasa a los siguientes turnos.
        
    huboaccion1 = 0
    huboenemigo = 0
    
    if finpartida == 1:
        break