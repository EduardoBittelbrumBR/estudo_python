# Faça um programa em python que abra e reproduza um áudio Mp3

import pygame

pygame.init()
pygame.mixer.music.load('maiden.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
