from car_colors import black, white
from car_message import message_setting
from default_game import *
import pygame
def defeated():
    GameImage.fill(black)
    #Text for pause and go
    largeText = pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect = message_setting("Game Over", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*3))
    GameImage.blit(TextSurf, TextRect)
    largeText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = message_setting("Esc - Quit, P - Start Over", largeText, white)
    TextRect.center = ((game_screen_x/2),((game_screen_y/8)*5))
    GameImage.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    x = 1
                    return x
                
                
        

        pygame.display.update()
        clock.tick(15)
