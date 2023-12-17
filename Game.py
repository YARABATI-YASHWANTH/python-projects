import pygame
import random

pygame.init()


window_width, window_height = 800, 400
ground_height = 350
fps = 60


white = (255, 255, 255)
black = (0, 0, 0)


game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dino Running Game")


dino_image = pygame.image.load('dino.jpg')
cactus_image = pygame.image.load('cactus.png')


dino_image = pygame.transform.scale(dino_image, (50, 50))
cactus_image = pygame.transform.scale(cactus_image, (30, 50))

game_clock = pygame.time.Clock()


dino_x, dino_y = 50, ground_height - 50
cactus_x, cactus_y = 20 + window_width, ground_height - 50
cactus_speed = 5
jump = False
jump_count = 10
running = True


while running:
    game_clock.tick(fps)
    game_window.fill(white)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True

    if jump:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.5 * neg
            jump_count =jump_count - 1
        else:
            jump = False
            jump_count = 10

    game_window.blit(dino_image, (dino_x, dino_y))
    game_window.blit(cactus_image, (cactus_x, cactus_y))

    cactus_x = cactus_x - cactus_speed
    if cactus_x < -30:
        cactus_x = window_width + 20
        cactus_y = ground_height - 50

    dino = pygame.Rect(dino_x, dino_y, 50, 50)
    cactus = pygame.Rect(cactus_x, cactus_y, 30, 50)
    if dino.colliderect(cactus):
        print("Game Over")
        running = False

    pygame.display.update()

pygame.quit() 