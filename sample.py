from operator import truediv
import pygame
from pygame import mixer
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invaders Game")

# score
score_value = 0

# player
playerImg = pygame.image.load("player.png")
playerX, playerY = 350, 500
playerX_change = 0

# enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 690)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 5, 40

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX, bulletY = 0, playerY
bulletX_change, bulletY_change = 0, 5
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+15, y+24))

def isCollition(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 30:
        return True
    else:
        return False

mixer.Sound("Happy_cat.mp3").play()
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    mixer.Sound("don.mp3").play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0


    # player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 700:
        playerX = 700
    
    # enemy
    if enemyY >= 390:
        break
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 5
        enemyY += enemyY_change
    elif enemyX >= 690:
        enemyX_change = -5
        enemyY += enemyY_change
    
    # collision
    collision = isCollition(enemyX, enemyY, bulletX, bulletY)
    if collision:
        mixer.Sound("gucha.mp3").play()
        bulletY = playerY
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, 690)
        enemyY = random.randint(50, 150)
    
    # bulletMove
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    # score
    font = pygame.font.SysFont(None, 32)
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (20, 50))

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


