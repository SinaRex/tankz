import pygame
import level1
import level2
import level3

# Colours constants in RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (200, 200, 0)
ORANGE = (255, 106, 0)
LIGHT_BLUE = (10, 190, 225)
PURPLE = (50, 5, 115)
GRAY = (157, 164, 166)
DARK_GRAY = (75, 75, 75)

# Display width and display height is set to 800 x 600
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

FPS = 60


def text_object(msg, color, font_type, font_size):
    """
    Make the text and return the text's rendered surface and its dimensions.
    """
    font = pygame.font.SysFont(font_type, font_size)
    text_surface = font.render(msg, True, color)

    return text_surface, text_surface.get_rect()


def text_to_centre_x(screen, msg, color, font_type, font_size, y_dis=10):
    """
    Creates a text with given message msg, color color, font size font_size ,
    y's component y_dis, and font type font_type on the centre column of the
    screen.
    """
    text_obj_info = text_object(msg, color, font_type, font_size)
    txt_surf = text_obj_info[0]
    txt_rect = text_obj_info[1]
    txt_rect.center = DISPLAY_WIDTH / 2, y_dis
    screen.blit(txt_surf, txt_rect)


def text_to_button(screen, msg, butt_rect, color, size, font_type):
    """
    Make a text for the button!
    """
    text_info = text_object(msg, color, font_type, size)
    txt_surf = text_info[0]
    txt_rect = text_info[1]
    txt_rect.center = butt_rect.center
    screen.blit(txt_surf, txt_rect)


def create_button(screen, msg, color, x, y, w, h, txt_color, txt_size, font_type):
    """
    Make a button and put a text on it.
    """
    butt_rect = pygame.draw.rect(screen, color, (x, y, w, h))
    text_to_button(screen, msg, butt_rect, txt_color, txt_size, font_type)


def level_selection(screen, clock):
    """
    Level selection.
    """
    menu_screen = False
    level_screen = True
    level_1 = False
    level_2 = False
    level_3 = False

    bg_level_1 = pygame.image.load("level_1_pic.png")
    bg_level_2 = pygame.image.load("level_2_pic.png")
    bg_level_3 = pygame.image.load("level_3_screen_pic.png")

    while level_screen:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(BLACK)

        if 20 <= mouse_pos[0] <= 20 + 100 and 20 <= mouse_pos[1] <= 20 + 100:
            pygame.draw.rect(screen, PURPLE, (10, 10, 120, 60))

        if 320 <= mouse_pos[0] <= 320 + 160 and 120 <= mouse_pos[1] <= 220:
            screen.blit(bg_level_1, (0, 0))
            pygame.draw.rect(screen, GREEN, (310, 110, 180, 120))

        if 320 <= mouse_pos[0] <= 320 + 160 and 260 <= mouse_pos[1] <= 360:
            screen.blit(bg_level_2, (0, 0))
            pygame.draw.rect(screen, GREEN, (310, 250, 180, 120))

        if 320 <= mouse_pos[0] <= 320 + 160 and 400 <= mouse_pos[1] <= 500:
            screen.blit(bg_level_3, (0, 0))
            pygame.draw.rect(screen, GREEN, (310, 390, 180, 120))

        font_type = "stencilstd"
        create_button(screen, "Back", RED, 20, 20, 100, 40, WHITE, 30, font_type)

        create_button(screen, "Level 1", WHITE, DISPLAY_WIDTH / 2 - 80, 120, 160, 100, BLACK, 20, font_type)
        create_button(screen, "Level 2", WHITE, DISPLAY_WIDTH / 2 - 80, 260, 160, 100, BLACK, 20, font_type)
        create_button(screen, "Level 3", WHITE, DISPLAY_WIDTH / 2 - 80, 400, 160, 100, BLACK, 20, font_type)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                if 20 <= mouse_pos[0] <= 20 + 100 and 20 <= mouse_pos[1] <= 20 + 100:
                    menu_screen = True
                    level_screen = False

                if 320 <= mouse_pos[0] <= 320 + 160 and 120 <= mouse_pos[1] <= 220:
                    level_screen = False
                    level_1 = True

                if 320 <= mouse_pos[0] <= 320 + 160 and 260 <= mouse_pos[1] <= 360:
                    level_screen = False
                    level_2 = True

                if 320 <= mouse_pos[0] <= 320 + 160 and 400 <= mouse_pos[1] <= 500:
                    level_screen = False
                    level_3 = True

        clock.tick(FPS)
        pygame.display.update()

    if menu_screen:
        start_menu(screen, clock)

    elif level_1:
        level1.start_level_1(screen, clock)

    elif level_2:
        level2.start_level_2(screen, clock)

    elif level_3:
        level3.start_level_3(screen, clock)


def start_menu(screen, clock):
    """
    Make and show the start menu
    """
    menu_screen = True
    about_screen = False
    level_screen = False

    while menu_screen:
        # Get the mouse positions. The type of mouse_pos is in tuple.
        mouse_pos = pygame.mouse.get_pos()

        # Fill the background with black.
        screen.fill(BLACK)

        # Make the title on the screen!
        font_type = "stencilstd"
        text_to_centre_x(screen, "TANKZ", GREEN, font_type, 100, 150)

        # Make the animation before the actual buttons; i.e. when the mouse
        # hovers on the buttons do the animation.
        if 90 <= mouse_pos[0] <= 90 + 160 and 350 <= mouse_pos[1] <= 450:
            pygame.draw.rect(screen, RED, (90 - 20, 350 - 20, 200, 140))

        if 320 <= mouse_pos[0] <= 320 + 160 and 350 <= mouse_pos[1] <= 450:
            pygame.draw.rect(screen, LIGHT_BLUE, (320 - 20, 350 - 20, 200, 140))

        if 550 <= mouse_pos[0] <= 550 + 160 and 350 <= mouse_pos[1] <= 450:
            pygame.draw.rect(screen, PURPLE, (550 - 20, 350 - 20, 200, 140))

        # Panning between button is 70px
        # Every button is 160px x 100px
        panning_butts = 70
        create_button(screen, "Start", BLUE, 320, 350, 160, 100, WHITE, 40, font_type)
        create_button(screen, "About", YELLOW, 320 - 160 - panning_butts, 350, 160, 100, WHITE, 40, font_type)
        create_button(screen, "Quit", RED, 480 + panning_butts, 350, 160, 100, WHITE, 40, font_type)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                if 90 <= mouse_pos[0] <= 90 + 160 and 350 <= mouse_pos[1] <= 450:
                    menu_screen = False
                    about_screen = True

                if 320 <= mouse_pos[0] <= 320 + 160 and 350 <= mouse_pos[1] <= 450:
                    pygame.draw.rect(screen, LIGHT_BLUE, (320 - 20, 350 - 20, 200, 140))
                    menu_screen = False
                    level_screen = True

                if 550 <= mouse_pos[0] <= 550 + 160 and 350 <= mouse_pos[1] <= 450:
                    menu_screen = False
                    pygame.quit()
                    exit(0)

        # Update the screen after each iteration of the loop.
        clock.tick(FPS)
        pygame.display.update()

    if level_screen:
        level_selection(screen, clock)

    elif about_screen:
        # TODO: finish the about screen!
        print("YO...don't forget to do this!")


def main():
    """
    Launches the game.
    """
    pygame.init()


    dis_size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
    screen = pygame.display.set_mode(dis_size)
    pygame.display.set_caption("TANKZ")

    # Setting the Frame per second (FPS) to 60
    clock = pygame.time.Clock()
    start_menu(screen, clock)


if __name__ == "__main__":
    main()
