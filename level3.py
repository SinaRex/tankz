import pygame
import tankz
import player1
import player2
import level1
import math
import random


NUM_ROCKETS = 10


def make_rockets():
    rocket_list = []

    for i in range(NUM_ROCKETS):
        x = random.randrange(0, tankz.DISPLAY_WIDTH - 4)
        y = random.randrange(-100, 0)
        speed_y = random.randrange(3, 7)
        rocket = pygame.Rect(x, y, 5, 50)
        rocket_list.append([rocket, speed_y])

    return rocket_list


def update_rockets(screen, rockets, p1_tank, p2_tank):
    blast_snd = pygame.mixer.Sound("sounds/explosion_Mike_Koenig.wav")
    for rocket in rockets:
        rocket[0].y += rocket[1]
        pygame.draw.rect(screen, tankz.ORANGE, rocket[0])
        if rocket[0].colliderect(p1_tank):
            blast_snd.play()
            player1.health -= 50
            rockets.remove(rocket)

        if rocket[0].colliderect(p2_tank):
            blast_snd.play()
            player2.health -= 50
            rockets.remove(rocket)

        if rocket[0].y > tankz.DISPLAY_HEIGHT:
            rockets.remove(rocket)


def start_level_3(screen, clock):
    shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")

    prev_time = pygame.time.get_ticks()
    rockets = []

    paused = False

    p1_angle = 180
    p1_tank, muzz_pos = player1.draw_tank(screen, tankz.DISPLAY_WIDTH - 200,
                                          tankz.DISPLAY_HEIGHT - 100, p1_angle)
    p1_bullets = []
    player1.health = 100
    player1.speed_r = 0
    player1.speed_l = 0
    player1.speed_u = 0
    player1.speed_d = 0
    player1.speed_angle_CW = 0
    player1.speed_angle_CCW = 0

    p2_angle = 0
    p2_tank, muzz_pos_2 = player2.draw_tank(screen, 90,
                                            100, p2_angle)
    p2_bullets = []
    player2.health = 100
    player2.speed_r = 0
    player2.speed_l = 0
    player2.speed_u = 0
    player2.speed_d = 0
    player2.speed_angle_CW = 0
    player2.speed_angle_CCW = 0

    bg_level_3 = pygame.image.load("level_3_pic.png")
    bg_level_3_walls = pygame.image.load("level_3_walls_pic.png")

    while True:
        screen.blit(bg_level_3, (0, 0))

        wall1 = pygame.Rect(476, 557, 545 - 476, 600 - 557)
        wall2 = pygame.Rect(471, 349, 543 - 471, 465 - 349)
        wall3 = pygame.Rect(471, 349, 674 - 471, 416 - 349)

        wall4 = pygame.Rect(94, 188, 300 - 94, 254 - 188)
        wall5 = pygame.Rect(226, 138, 300 - 255, 254 - 138)
        wall6 = pygame.Rect(222, 0, 286 - 222, 49)

        WALL_LIST = [wall1, wall2, wall3, wall4, wall5, wall6]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:

                # Player 1 keys
                if event.key == pygame.K_UP:
                    player1.speed_u = -3

                if event.key == pygame.K_RIGHT:
                    player1.speed_r = 3

                if event.key == pygame.K_DOWN:
                    player1.speed_d = 3

                if event.key == pygame.K_LEFT:
                    player1.speed_l = -3

                if event.key == pygame.K_COMMA:
                    player1.speed_angle_CW = -1.9

                if event.key == pygame.K_PERIOD:
                    player1.speed_angle_CCW = 1.9

                # Player 2 keys
                if event.key == pygame.K_w:
                    player2.speed_u = -3

                if event.key == pygame.K_d:
                    player2.speed_r = 3

                if event.key == pygame.K_s:
                    player2.speed_d = 3

                if event.key == pygame.K_a:
                    player2.speed_l = -3

                if event.key == pygame.K_c:
                    player2.speed_angle_CW = -1.9

                if event.key == pygame.K_v:
                    player2.speed_angle_CCW = 1.9

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
                                if len(p1_bullets) > 0:
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
                                if len(p2_bullets) > 0:
                                    p2_bullets.remove(bullet)

        p1_angle = player1.update_movement(p1_tank, WALL_LIST, p1_angle)
        p2_angle = player2.update_movement(p2_tank, WALL_LIST, p2_angle)

        for bullet in p1_bullets:
            bul_rect = player1.shoot(screen, bullet, WALL_LIST)
            level1.check_collision(bul_rect, bullet, p1_tank, p2_tank)
            if bullet[3] == 3:
                level1.bullet_explosion(screen, p1_bullets, bullet)

        for bullet in p2_bullets:
            bul_rect = player2.shoot(screen, bullet, WALL_LIST)
            level1.check_collision(bul_rect, bullet, p1_tank, p2_tank)
            if bullet[3] == 3:
                level1.bullet_explosion(screen, p2_bullets, bullet)

        p1_tank, muzz_pos = player1.draw_tank(screen, p1_tank.x, p1_tank.y,
                                              p1_angle)

        p2_tank, muzz_pos_2 = player2.draw_tank(screen, p2_tank.x, p2_tank.y,
                                                p2_angle)

        screen.blit(bg_level_3_walls, (0, 0))

        cur_time = pygame.time.get_ticks()
        if (cur_time - prev_time) > 12000:
            prev_time = cur_time
            rockets += make_rockets()

        if len(rockets) > 0:
            update_rockets(screen, rockets, p1_tank, p2_tank)

        level1.draw_health_bars(screen)

        if player1.health <= 0 and player2.health <= 0:
            level1.display_winner(screen, clock, "TIE", start_level_3)
        elif player1.health <= 0:
            level1.display_winner(screen, clock, "RED", start_level_3)
        elif player2.health <= 0:
            level1.display_winner(screen, clock, "BLUE", start_level_3)

        if paused:
            paused = level1.pause(screen, clock, start_level_3)

        # prev_time = cur_time
        # cur_time = pygame.time.get_ticks()
        # if cur_time - prev_time < 500:
        #     rockets += make_rockets(screen)



        clock.tick(tankz.FPS)
        pygame.display.update()
