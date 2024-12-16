import os, pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
os.environ['SDL_AUDIODRIVER'] = 'pulse'

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width - 10, screen_height - 50), pygame.RESIZABLE)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#image declaration-

back = pygame.image.load("assets/Puzzle.png")
background = pygame.transform.scale(back, (screen_width, screen_height))
