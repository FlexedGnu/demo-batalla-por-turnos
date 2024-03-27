import pygame
import winsound
import time

pygame.mixer.init()

print("ZA WARUDO! TOKI WO TOMARE!!")
winsound.PlaySound("zawarudo.wav", winsound.SND_ASYNC)
time.sleep(1.5)
winsound.PlaySound("tokiwo.wav", winsound.SND_ASYNC)
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