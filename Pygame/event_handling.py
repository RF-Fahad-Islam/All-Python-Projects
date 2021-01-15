import pygame
pygame.init()
gamewindow = pygame.display.set_mode((600,300))
pygame.display.set_caption("Event Handling")
exit_game = False
game_over = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            print(event.type)
            print(pygame.QUIT)
        if event.type == pygame.KEYDOWN:
            print(event.type)
            print(pygame.KEYDOWN)
            if event.key == pygame.K_RIGHT:
                print("You pressed the right arrow key")
                print(pygame.K_RIGHT)
                print(event.key)
pygame.quit()
quit()