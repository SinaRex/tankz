import pygame
import tankz
import player1
import player2
import level1
import math


def start_level_2(screen, clock):
    shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")

    WALL_1 = pygame.Rect(tankz.DISPLAY_WIDTH / 2 - 200,
                         tankz.DISPLAY_HEIGHT / 2 - 50, 400, 100)

    WALL_2 = pygame.Rect(tankz.DISPLAY_WIDTH / 2 - 50,
                         tankz.DISPLAY_HEIGHT / 2 - 200, 100, 400)

    WALL_LIST = [WALL_1, WALL_2]


    paused = False

    p1_angle = 180
    p1_tank, muzz_pos = player1.draw_tank(screen, tankz.DISPLAY_WIDTH - 80,
                                          100, p1_angle)
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
                                            tankz.DISPLAY_HEIGHT - 100, p2_angle)
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
        pygame.draw.rect(screen, tankz.DARK_GRAY, WALL_1)
        pygame.draw.rect(screen, tankz.DARK_GRAY, WALL_2)

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


        level1.draw_health_bars(screen)

        if player1.health <= 0 and player2.health <= 0:
            level1.display_winner(screen, clock, "TIE", start_level_2)
        elif player1.health <= 0:
            level1.display_winner(screen, clock, "RED", start_level_2)
        elif player2.health <= 0:
            level1.display_winner(screen, clock, "BLUE", start_level_2)

        if paused:
            paused = level1.pause(screen, clock, start_level_2)

        clock.tick(tankz.FPS)
        pygame.display.update()
