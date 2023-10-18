import pygame
import random

clock = pygame.time.Clock()
clock.tick(30)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

snake_position = [100, 50]
 
# defining first 4 blocks of snake
# body
snake_body = [[100, 50],[90, 50],[80, 50],[70, 50]]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    snake_body.pop()
    snake_body.insert(0, [110, 60])
    for i in snake_body:
      pygame.draw.rect(screen, "green", pygame.Rect(i[0], i[1], 50, 50))
    
    #https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/

    keys = pygame.key.get_pressed()u
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        snake_body.pop()
        snake_body.insert(0, [110, ])
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        snake_position[1] += 10
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        snake_position[0] -= 10
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        snake_position[0] += 10

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()