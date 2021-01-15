import pygame
import random
pygame.init()

#Height and Width
screen_width = 600
screen_height = 300
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
#Define Colors 
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#Define variables
exit_game = False
game_over = False
score = 0

snake_x = 55
snake_y = 30
velocity_x = 5
velocity_y = 5
velocity_init = 5
snake_size = 10

food_x = random.randint(6,screen_width)
food_y = random.randint(6,screen_height)
fps = 60
clock = pygame.time.Clock()
#Create the game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x += 5
                velocity_x = velocity_init
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                snake_x -= 5
                velocity_x = -velocity_init
                velocity_y = 0
            if event.key == pygame.K_DOWN:
                snake_y += 5
                velocity_y = velocity_init
                velocity_x = 0
            if event.key == pygame.K_UP:
                snake_y -= 5
                velocity_y = -velocity_init
                velocity_x = 0
                
    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
        score += 1
        print(f"Score : {score*10}")
        food_x = random.randint(6,screen_width)
        food_y = random.randint(6,screen_height)

    snake_x += velocity_x
    snake_y += velocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()