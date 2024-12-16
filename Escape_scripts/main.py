import pygame, sys
from button import ButtonBordered, Button
from constants import *


def menus():
    def main_menu():
        while True:
            screen.blit(background, (0,0))

            main_menu_pos = pygame.mouse.get_pos()

            menu_text = get_font(100).render("Escape", True, "#db0d0d")
            menu_rect = menu_text.get_rect(center=(screen_width / 2, screen_height / 13))

            play_button = ButtonBordered(image= None, pos=(screen_width / 2, screen_height / 5),
                                 text_input="Enter", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            question_button = ButtonBordered(image=None, pos=(screen_width / 2, screen_height / 1.25),
                                         text_input="?", font=get_font(200), base_color="#d7fcd4",hovering_color="White")
            options_button = ButtonBordered(image=None, pos=(screen_width / 2, screen_height / 3.2),
                                         text_input="options", font=get_font(75), base_color="#d7fcd4",hovering_color="White")
            levels_button = ButtonBordered(image=None, pos=(screen_width / 2, screen_height / 2.3),
                                         text_input="levels", font=get_font(75), base_color="#d7fcd4",hovering_color="White")
            giveup_button = ButtonBordered(image=None, pos=(screen_width / 2, screen_height / 1.8),
                                           text_input="give up", font=get_font(75), base_color="#d7fcd4",
                                           hovering_color="White")

            screen.blit(menu_text, menu_rect)

            play_button.changeColor(main_menu_pos)
            question_button.changeColor(main_menu_pos)
            options_button.changeColor(main_menu_pos)
            levels_button.changeColor(main_menu_pos)
            giveup_button.changeColor(main_menu_pos)

            play_button.update(screen)
            question_button.update(screen)
            options_button.update(screen)
            levels_button.update(screen)
            giveup_button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    main_menu()
menus()