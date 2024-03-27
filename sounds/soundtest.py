import winsound
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.mixer.init()

sound = pygame.mixer.Sound("music.wav")

sound.play(loops=-1)

print("Prueba de sonidos")
while True:
    sfxinput = input("Presiona enter para hacer un sonido. ")
    if sfxinput == "":
        sfx = random.randint(0,6)
        if sfx == 0:
            winsound.PlaySound("tuturno.wav",winsound.SND_ASYNC)
        elif sfx == 1:
            winsound.PlaySound("ataque.wav",winsound.SND_ASYNC)
        elif sfx == 2:
            winsound.PlaySound("atkfuerte.wav",winsound.SND_ASYNC)
        elif sfx == 3:
            winsound.PlaySound("atkplus.wav",winsound.SND_ASYNC)
        elif sfx == 4:
            winsound.PlaySound("cura.wav",winsound.SND_ASYNC)
        elif sfx == 5:
            winsound.PlaySound("daño.wav",winsound.SND_ASYNC)
        elif sfx == 6:
            winsound.PlaySound("defender.wav",winsound.SND_ASYNC)
    elif sfxinput == "exit":
        break