import pygame
import math
import tankz

health = 100


speed_r = 0
speed_l = 0
speed_u = 0
speed_d = 0
speed_angle_CW = 0
speed_angle_CCW = 0

width = 50
height = 50

bullet_speed = 7

# Muzzle's information
R = 40



def draw_tank(screen, x, y, angle_d):
    body = pygame.draw.rect(screen, tankz.BLACK, (x, y, width, height))
    pygame.draw.circle(screen, tankz.BLUE, body.center, 15)

    # Change degree to radians
    angle_r = (math.pi * angle_d) / 180

    # Used Polar coordinates for the circular motion of the muzzle.
    muzz_x = body.center[0] + R * math.cos(angle_r)
    muzz_y = body.center[1] + R * math.sin(angle_r)
    line = pygame.draw.line(screen, tankz.BLUE, (muzz_x, muzz_y), body.center, 7)

    return [body, (int(muzz_x), int(muzz_y))]


def update_movement(p1_tank, wall_list, p1_angle):
    p1_tank.x += speed_r if speed_r != 0 else speed_l

    # Checking for collision
    for wall in wall_list:
        if p1_tank.colliderect(wall):
            if speed_l < 0:
                p1_tank.left = wall.right
            if speed_r > 0:
                p1_tank.right = wall.left

    p1_tank.y += speed_u if speed_u != 0 else speed_d

    # Checking for collision
    for wall in wall_list:
        if p1_tank.colliderect(wall):
            if speed_u < 0:
                p1_tank.top = wall.bottom
            elif speed_d > 0:
                p1_tank.bottom = wall.top

    p1_angle += speed_angle_CW if speed_angle_CW != 0 else speed_angle_CCW

    # Set the boundaries.
    if p1_tank.x < 0:
        p1_tank.x = 0

    if p1_tank.x + p1_tank.width > tankz.DISPLAY_WIDTH:
        p1_tank.x = tankz.DISPLAY_WIDTH - width

    if p1_tank.y < 0:
        p1_tank.y = 0

    if p1_tank.y + height > tankz.DISPLAY_HEIGHT:
        p1_tank.y = tankz.DISPLAY_HEIGHT - height

    return p1_angle


def shoot(screen, bullet, wall_list):
    bounce_snd = pygame.mixer.Sound("sounds/bounce.wav")

    bul_rect = pygame.draw.circle(screen, tankz.RED, bullet[0], 4)

    if bullet[0][0] <= 0:
        bullet[4] *= -1
        bullet[3] += 1
        bounce_snd.play()

    if bullet[0][0] >= tankz.DISPLAY_WIDTH:
        bullet[4] *= -1
        bullet[3] += 1
        bounce_snd.play()

    if bullet[0][1] <= 0:
        bullet[5] *= -1
        bullet[3] += 1
        bounce_snd.play()

    if bullet[0][1] >= tankz.DISPLAY_HEIGHT:
        bullet[5] *= -1
        bullet[3] += 1
        bounce_snd.play()


    bullet[0][0] += bullet[4]
    # Checking for collision in x direction
    for wall in wall_list:
        if (wall.left <= bullet[0][0] <= wall.right and
                        wall.top <= bullet[0][1] <= wall.bottom):
            bullet[4] *= -1
            bullet[0][0] += bullet[4]
            bullet[3] += 1
            bounce_snd.play()


    bullet[0][1] += bullet[5]
    # Checking for collision in y direction
    for wall in wall_list:
        if (wall.left <= bullet[0][0] <= wall.right and
                        wall.top <= bullet[0][1] <= wall.bottom):
            bullet[5] *= -1
            bullet[0][1] += bullet[5]
            bullet[3] += 1
            bounce_snd.play()

    return bul_rect








