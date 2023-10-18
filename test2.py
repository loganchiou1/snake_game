import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
apples = 1

pygame.draw.rect(screen, "green", pygame.Rect(50, 50, 50, 50))
pygame.time.wait(apples*50)