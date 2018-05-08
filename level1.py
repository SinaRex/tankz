import pygame
import math
import tankz

import player1
import player2
import random

# (X, Y, W, H)
WALL_EAST_DIM = pygame.Rect(tankz.DISPLAY_WIDTH - 200 - 100, 130, 100, 250)
WALL_WEST_DIM = pygame.Rect(200, tankz.DISPLAY_HEIGHT / 2 - 50, 100, 250)
WALL_LIST = [WALL_EAST_DIM, WALL_WEST_DIM]



def pause(screen, clock, level_to_start):
    is_paused = True
    font_type = "stencilstd"
    button_selected = 0

    player1.speed_r = 0
    player1.speed_l = 0
    player1.speed_u = 0
    player1.speed_d = 0
    player1.speed_angle_CW = 0
    player1.speed_angle_CCW = 0

    player2.speed_r = 0
    player2.speed_l = 0
    player2.speed_u = 0
    player2.speed_d = 0
    player2.speed_angle_CW = 0
    player2.speed_angle_CCW = 0


    while is_paused:
        box_rect = pygame.Rect(0, 0, 500, tankz.DISPLAY_HEIGHT - 100)
        box_rect.center = (tankz.DISPLAY_WIDTH / 2, tankz.DISPLAY_HEIGHT / 2)
        pygame.draw.rect(screen, tankz.BLACK, box_rect)

        text_winner = tankz.text_object("PAUSED", tankz.GREEN, font_type, 70)
        text_winner[1].centerx = box_rect.centerx
        text_winner[1].y = 100
        screen.blit(text_winner[0], text_winner[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

                if event.key == pygame.K_DOWN:
                    button_selected += 1

                if event.key == pygame.K_UP:
                    if button_selected == 0:
                        button_selected = 3
                    button_selected -= 1

                if event.key == pygame.K_RETURN:
                    if button_selected == 0:
                        level_to_start(screen, clock)

                    if button_selected == 1:
                        tankz.start_menu(screen, clock)

                    if button_selected == 2:
                        pygame.quit()
                        exit(0)

        button_selected %= 3

        if button_selected == 0:
            pygame.draw.rect(screen, tankz.GREEN, (310, 240, 160 + 20, 50 + 20))

        elif button_selected == 1:
            pygame.draw.rect(screen, tankz.GREEN, (310, 330, 160 + 20, 50 + 20))

        elif button_selected == 2:
            pygame.draw.rect(screen, tankz.GREEN, (310, 420, 160 + 20, 50 + 20))


        tankz.create_button(screen, "REMATCH", tankz.WHITE, box_rect.centerx - 80, 250, 160, 50,
                            tankz.BLACK, 20, font_type)

        tankz.create_button(screen, "MAIN MEUN", tankz.WHITE, box_rect.centerx - 80, 250 + 10 + 50 + 30, 160, 50,
                            tankz.BLACK, 20, font_type)

        tankz.create_button(screen, "QUIT", tankz.WHITE, box_rect.centerx - 80, 340 + 10 + 50 + 30, 160, 50,
                            tankz.BLACK, 20, font_type)

        pygame.display.update()


def display_winner(screen, clock, which, level_to_start):
    this_screen = True
    button_selected = 0

    blast_snd = pygame.mixer.Sound("sounds/tank_blast_Mike_Koenig.wav")
    trumpets = pygame.mixer.Sound("sounds/Trumpets.wav")
    trumpets.play()
    blast_snd.play()

    color = None
    msg = ""
    font_type = "stencilstd"

    if which == "BLUE":
        color = tankz.BLUE
        msg = which + " WON!"
    elif which == "RED":
        color = tankz.RED
        msg = which + " WON!"

    elif which == "TIE":
        color = tankz.YELLOW
        msg = which + "!"

    while this_screen:
        box_rect = pygame.Rect(0, 0, 500, tankz.DISPLAY_HEIGHT - 100)
        box_rect.center = (tankz.DISPLAY_WIDTH / 2, tankz.DISPLAY_HEIGHT / 2)
        pygame.draw.rect(screen, tankz.BLACK, box_rect)

        text_winner = tankz.text_object(msg, color, font_type, 70)
        text_winner[1].centerx = box_rect.centerx
        text_winner[1].y = 100
        screen.blit(text_winner[0], text_winner[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    button_selected += 1

                if event.key == pygame.K_UP:
                    if button_selected == 0:
                        button_selected = 3
                    button_selected -= 1

                if event.key == pygame.K_RETURN:
                    if button_selected == 0:
                        level_to_start(screen, clock)

                    if button_selected == 1:
                        tankz.start_menu(screen, clock)

                    if button_selected == 2:
                        pygame.quit()
                        exit(0)

        button_selected %= 3

        if button_selected == 0:
            pygame.draw.rect(screen, color, (310, 240, 160 + 20, 50 + 20))

        elif button_selected == 1:
            pygame.draw.rect(screen, color, (310, 330, 160 + 20, 50 + 20))

        elif button_selected == 2:
            pygame.draw.rect(screen, color, (310, 420, 160 + 20, 50 + 20))


        tankz.create_button(screen, "REMATCH", tankz.WHITE, box_rect.centerx - 80, 250, 160, 50,
                            tankz.BLACK, 20, font_type)

        tankz.create_button(screen, "MAIN MEUN", tankz.WHITE, box_rect.centerx - 80, 250 + 10 + 50 + 30, 160, 50,
                            tankz.BLACK, 20, font_type)

        tankz.create_button(screen, "QUIT", tankz.WHITE, box_rect.centerx - 80, 340 + 10 + 50 + 30, 160, 50,
                            tankz.BLACK, 20, font_type)

        pygame.display.update()


def draw_health_bars(screen):

    box_1 = pygame.draw.rect(screen, tankz.WHITE, (tankz.DISPLAY_WIDTH - 30 - 120,
                                           30, 120, 30))

    font_type = "stencilstd"
    text_surf_1 = tankz.text_object("BLUE", tankz.BLUE, font_type, 20)
    text_surf_1[1].centerx = box_1.centerx
    text_surf_1[1].y = 10
    screen.blit(text_surf_1[0], text_surf_1[1])

    if player1.health > 0:
        pygame.draw.rect(screen, tankz.GREEN, (tankz.DISPLAY_WIDTH - 35 - (player1.health + 10),
                                               35, player1.health + 10, 20))

    box_2 = pygame.draw.rect(screen, tankz.WHITE, (30, 30, 120, 30))
    text_surf_2 = tankz.text_object("RED", tankz.RED, font_type, 20)
    text_surf_2[1].centerx = box_2.centerx
    text_surf_2[1].y = 10
    screen.blit(text_surf_2[0], text_surf_2[1])

    if player2.health > 0:
        pygame.draw.rect(screen, tankz.GREEN, (35, 35, player2.health + 10, 20))




def bullet_explosion(screen, p1_bullets, bullet):
    if 0 <= bullet[6] < 3:
        blast_snd = pygame.mixer.Sound("sounds/explosion_Mike_Koenig.wav")
        blast_snd.play()
        bullet[4] = bullet[5] = 0
        pygame.draw.circle(screen, tankz.RED, bullet[0], 7)

    elif 3 <= bullet[6] < 6 :
        pygame.draw.circle(screen, tankz.ORANGE, bullet[0], 12)
        pygame.draw.circle(screen, tankz.RED, bullet[0], 7)

        for i in range(6):
            pygame.draw.circle(screen, tankz.DARK_GRAY, (bullet[0][0] - random.randrange(-30, 30),
                                                     bullet[0][1] - random.randrange(-20, 20)), random.randrange(4, 6))

    elif 6 <= bullet[6] <= 9:
        pygame.draw.circle(screen, tankz.YELLOW, bullet[0], random.randrange(16, 20))
        pygame.draw.circle(screen, tankz.ORANGE, bullet[0], random.randrange(8, 15))
        pygame.draw.circle(screen, tankz.RED, bullet[0], random.randrange(3, 7))

        for i in range(3):
            pygame.draw.circle(screen, tankz.DARK_GRAY, (bullet[0][0] - random.randrange(-20, 20),
                                                     bullet[0][1] - random.randrange(-20, 20)), random.randrange(1, 3))

    else:
        p1_bullets.remove(bullet)

    bullet[6] += 1


def check_collision(bul_rect, bullet, p1_tank, p2_tank):
    blast_snd = pygame.mixer.Sound("sounds/explosion_Mike_Koenig.wav")
    if bul_rect.colliderect(p1_tank):
        blast_snd.play()
        bullet[3] = 3
        bullet[6] = 10
        player1.health -= 50

    if bul_rect.colliderect(p2_tank):
        blast_snd.play()
        bullet[3] = 3
        bullet[6] = 10
        player2.health -= 50


def start_level_1(screen, clock):
    shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")

    paused = False

    p1_angle = 180
    p1_tank, muzz_pos = player1.draw_tank(screen, tankz.DISPLAY_WIDTH - 80,
                                          tankz.DISPLAY_HEIGHT / 2, p1_angle)
    p1_bullets = []
    player1.health = 100
    player1.speed_r = 0
    player1.speed_l = 0
    player1.speed_u = 0
    player1.speed_d = 0
    player1.speed_angle_CW = 0
    player1.speed_angle_CCW = 0

    p2_angle = 0
    p2_tank, muzz_pos_2 = player2.draw_tank(screen, 80,
                                            tankz.DISPLAY_HEIGHT / 2, p2_angle)
    p2_bullets = []
    player2.health = 100
    player2.speed_r = 0
    player2.speed_l = 0
    player2.speed_u = 0
    player2.speed_d = 0
    player2.speed_angle_CW = 0
    player2.speed_angle_CCW = 0

    while True:
        screen.fill(tankz.GRAY)
        pygame.draw.rect(screen, tankz.DARK_GRAY, WALL_EAST_DIM)
        pygame.draw.rect(screen, tankz.DARK_GRAY, WALL_WEST_DIM)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:

                # Player 1 keys
                if event.key == pygame.K_UP:
                    player1.speed_u = -2

                if event.key == pygame.K_RIGHT:
                    player1.speed_r = 2

                if event.key == pygame.K_DOWN:
                    player1.speed_d = 2

                if event.key == pygame.K_LEFT:
                    player1.speed_l = -2

                if event.key == pygame.K_COMMA:
                    player1.speed_angle_CW = -1.7

                if event.key == pygame.K_PERIOD:
                    player1.speed_angle_CCW = 1.7

                # Player 2 keys
                if event.key == pygame.K_w:
                    player2.speed_u = -2

                if event.key == pygame.K_d:
                    player2.speed_r = 2

                if event.key == pygame.K_s:
                    player2.speed_d = 2

                if event.key == pygame.K_a:
                    player2.speed_l = -2

                if event.key == pygame.K_c:
                    player2.speed_angle_CW = -1.7

                if event.key == pygame.K_v:
                    player2.speed_angle_CCW = 1.7

                # pause
                if event.key == pygame.K_ESCAPE:
                    paused = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player1.speed_u = 0

                if event.key == pygame.K_RIGHT:
                    player1.speed_r = 0

                if event.key == pygame.K_DOWN:
                    player1.speed_d = 0

                if event.key == pygame.K_LEFT:
                    player1.speed_l = 0

                if event.key == pygame.K_COMMA:
                    player1.speed_angle_CW = 0

                if event.key == pygame.K_PERIOD:
                    player1.speed_angle_CCW = 0

                if event.key == pygame.K_SLASH:
                    if len(p1_bullets) < 3:
                        shoot_sound.play()
                        rad = math.radians(p1_angle)
                        speed_x = int(10 * math.cos(rad))
                        speed_y = int(10 * math.sin(rad))
                        bullet = [[muzz_pos[0], muzz_pos[1]], p1_angle, muzz_pos, 0, speed_x, speed_y, 0]
                        if not(muzz_pos[1] <= 0):
                            p1_bullets.append(bullet)
                        for wall in WALL_LIST:
                            if wall.left < muzz_pos[0] < wall.right and wall.top < muzz_pos[1] < wall.bottom:
                                p1_bullets.remove(bullet)
                # Player 2 keys
                if event.key == pygame.K_w:
                    player2.speed_u = 0

                if event.key == pygame.K_d:
                    player2.speed_r = 0

                if event.key == pygame.K_s:
                    player2.speed_d = 0

                if event.key == pygame.K_a:
                    player2.speed_l = 0

                if event.key == pygame.K_c:
                    player2.speed_angle_CW = 0

                if event.key == pygame.K_v:
                    player2.speed_angle_CCW = 0

                if event.key == pygame.K_SPACE:
                    if len(p2_bullets) < 3:
                        shoot_sound.play()
                        rad = math.radians(p2_angle)
                        speed_x = int(10 * math.cos(rad))
                        speed_y = int(10 * math.sin(rad))
                        bullet = [[muzz_pos_2[0], muzz_pos_2[1]], p2_angle, muzz_pos_2, 0, speed_x, speed_y, 0]
                        if not(muzz_pos_2[1] <= 0):
                            p2_bullets.append(bullet)
                        for wall in WALL_LIST:
                            if wall.left < muzz_pos_2[0] < wall.right and wall.top < muzz_pos_2[1] < wall.bottom:
                                p2_bullets.remove(bullet)

        p1_angle = player1.update_movement(p1_tank, WALL_LIST, p1_angle)
        p2_angle = player2.update_movement(p2_tank, WALL_LIST, p2_angle)

        for bullet in p1_bullets:
            bul_rect = player1.shoot(screen, bullet, WALL_LIST)
            check_collision(bul_rect, bullet, p1_tank, p2_tank)
            if bullet[3] == 3:
                bullet_explosion(screen, p1_bullets, bullet)

        for bullet in p2_bullets:
            bul_rect = player2.shoot(screen, bullet, WALL_LIST)
            check_collision(bul_rect, bullet, p1_tank, p2_tank)
            if bullet[3] == 3:
                bullet_explosion(screen, p2_bullets, bullet)

        p1_tank, muzz_pos = player1.draw_tank(screen, p1_tank.x, p1_tank.y,
                                              p1_angle)

        p2_tank, muzz_pos_2 = player2.draw_tank(screen, p2_tank.x, p2_tank.y,
                                                p2_angle)

        draw_health_bars(screen)

        if player1.health <= 0 and player2.health <= 0:
            display_winner(screen, clock, "TIE", start_level_1)
        elif player1.health <= 0:
            display_winner(screen, clock, "RED", start_level_1)
        elif player2.health <= 0:
            display_winner(screen, clock, "BLUE", start_level_1)

        if paused:
            paused = pause(screen, clock, start_level_1)

        clock.tick(tankz.FPS)
        pygame.display.update()



