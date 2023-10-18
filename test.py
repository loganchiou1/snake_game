import pygame
import random
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
xy = 0
direction = 50
snake_position = [100, 50]
apple = [random.randint(1, 25) * 50, random.randint(1, 14) * 50]

snake_body = [[100, 50], [100, 100]]

while running:

  time.sleep(0.5)
  # poll for events
  # pygame.QUIT event means the user clicked X to close your window
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  snake_head = snake_body[0].copy()
  snake_tail = snake_body[-1]  #last in array list thing
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    snake_head[1] -= 50
    xy = 1
    direction = -50

  elif keys[pygame.K_DOWN]:
    snake_head[1] += 50
    xy = 1
    direction = 50

  elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
    snake_head[0] -= 50
    xy = 0
    direction = -50

  elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
    snake_head[0] -= 50
    xy = 0
    direction = -50

  elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
    snake_head[0] += 50
    xy = 0
    direction = 50

  elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
    snake_head[0] += 50
    xy = 0
    direction = 50

  elif keys[pygame.K_LEFT]:
    snake_head[0] -= 50
    xy = 0
    direction = -50

  elif keys[pygame.K_RIGHT]:
    snake_head[0] += 50
    xy = 0
    direction = 50

  else:
    snake_head[xy] += direction

  #change for snake growing behavior

  #snake_body = [snake_head, snake_body[:-1]]

  # fill the screen with a color to wipe away anything from last frame

  screen.fill("black")

  snake_body = [snake_head] + snake_body
  

  #apple
  pygame.draw.rect(screen, "red", pygame.Rect(apple[0], apple[1], 50, 50))
  if (snake_head[0] == apple[0] and snake_head[1] == apple[1]):
    apple = [random.randint(1, 25) * 50, random.randint(1, 14) * 50]
    for block in snake_body:  # block is only index
      pygame.draw.rect(screen, "green", pygame.Rect(block[0], block[1], 50,
                                                    50))

  else:
    snake_body = snake_body[:-1]
    for block in snake_body:  # block is only index
      pygame.draw.rect(screen, "green", pygame.Rect(block[0], block[1], 50,
                                                    50))

  #https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/

  # flip() the display to put your work on screen
  pygame.display.update()

  # limits FPS to 60
  # dt is delta time in seconds since last frame, used for framerate-
  # independent physics.
  dt = clock.tick(15)
pygame.quit()