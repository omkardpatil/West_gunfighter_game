import pygame
import os
import random
# 1st thing is to create window aka surface

win_h = 500
win_w = 800

bg_color = (231, 213, 189)

fb_scale = (60, 75)
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Cowboy_save_yourself_game")
hit_wall = pygame.USEREVENT+1
fire_ball_vel = 4
fbvx = random.randrange(5, fire_ball_vel * 10)
fbvx = float(fbvx) / 10
fb_vel_xy = [fbvx, fire_ball_vel - fbvx]

fire_ball_pic = pygame.image.load(os.path.join('game_data2', 'fire_ball.png'))
fire_ball_pic = pygame.transform.scale(fire_ball_pic, fb_scale)
fire_balls=[]
acc_per_level=0.1

def fireball_fire():
    h = random.randint(5, win_h - fire_ball_pic.get_height())
    w = 30
    fb = pygame.Rect(w, h, fb_scale[0], fb_scale[1])
    fire_balls.append(fb)
    fbvx = random.randrange(5, fire_ball_vel * 10)
    fbvx = float(fbvx) / 10
    fb_vel_xy = [fbvx, fire_ball_vel - fbvx]


def fireball_movement(level):
    for fb in fire_balls:
        fb.x += (fb_vel_xy[0]+acc_per_level*level)
        fb.y += (fb_vel_xy[1]+acc_per_level*level)

def draw_display( fire_balls):

    for fb in fire_balls:
        win.blit(fire_ball_pic, (fb.x, fb.y))

    pygame.display.update()

def game_initialize():
    clock = pygame.time.Clock()
    # rectangle for storing and manipulating position of men
    fireball = pygame.Rect(win_w-30, win_h / 2, fb_scale[0], fb_scale[1])

    run = True
    level = 0
    return clock, run, fireball,level

def action(fire_ball):
    for fb in fire_ball:
        if fb.x > win_w:
            fire_ball.remove(fb)
        elif fb.y < 0 or fb.y > win_h-fb[3]:
            pygame.event.post(pygame.event.Event(hit_wall))


def main():  # main game login will be here
    clock, run, fireball,level = game_initialize()
    while run:
        # fps setting
        clock.tick(60)
        # pygame.event:?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == hit_wall:
                fb_vel_xy[1] = -fb_vel_xy[1]
        if len(fire_balls)<1:
            fireball_fire()

        # make display white, update
        fireball_movement(level)
        action(fire_balls)
        # print(len(bullets_l), len(bullets_r))
        draw_display(fire_balls)

    pygame.quit()
    # main() if u want to restart


# if one runs this file (pygame_learning.py) then this is true
if __name__ == "__main__":
    main()
