import pygame
import math
import tankz
import player1

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
    pygame.draw.circle(screen, tankz.RED, body.center, 15)

    angle_r = (math.pi * angle_d) / 180
    muzz_x = body.center[0] + R * math.cos(angle_r)
    muzz_y = body.center[1] + R * math.sin(angle_r)
    line = pygame.draw.line(screen, tankz.RED, (muzz_x, muzz_y), body.center, 7)

    return [body, (int(muzz_x), int(muzz_y))]


def update_movement(p2_tank, wall_list, p2_angle):
    p2_tank.x += speed_r if speed_r != 0 else speed_l

    # Checking for collision
    for wall in wall_list:
        if p2_tank.colliderect(wall):
            if speed_l < 0:
                p2_tank.left = wall.right
            if speed_r > 0:
                p2_tank.right = wall.left

    p2_tank.y += speed_u if speed_u != 0 else speed_d

    # Checking for collision
    for wall in wall_list:
        if p2_tank.colliderect(wall):
            if speed_d > 0:
                p2_tank.bottom = wall.top

            if speed_u < 0:
                p2_tank.top = wall.bottom

    p2_angle += speed_angle_CW if speed_angle_CW != 0 else speed_angle_CCW

    # Set the boundaries.
    if p2_tank.x < 0:
        p2_tank.x = 0

    if p2_tank.x + p2_tank.width > tankz.DISPLAY_WIDTH:
        p2_tank.x = tankz.DISPLAY_WIDTH - width

    if p2_tank.y < 0:
        p2_tank.y = 0

    if p2_tank.y + height > tankz.DISPLAY_HEIGHT:
        p2_tank.y = tankz.DISPLAY_HEIGHT - height

    return p2_angle


def shoot(screen, bullet, wall_list):
    # The code is repetitive
    return player1.shoot(screen, bullet, wall_list)
