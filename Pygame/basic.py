import pygame
# import time
pygame.init()
# print(x)
gamewindow = pygame.display.set_mode((1200,600))
pygame.display.set_caption("My First Game")

exit_game = False
game_over = False
li = [1,2,3,4,5,6,7,8,9,0]
print(li[:-1])

while not exit_game:
    # time.sleep(3)
    for event in pygame.event.get():
        print(event)
        
pygame.quit()
quit()