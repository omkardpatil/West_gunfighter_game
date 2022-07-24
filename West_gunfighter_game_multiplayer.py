import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

vel = 4
bullet_vel = 7
ult_vel=20
max_bullets = 6
max_health = 10



# 1st thing is to create window aka surface
multiplier=80
win_h = 9*multiplier
win_w = 16*multiplier

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("West_gunfighter_game_multiplayer")
pygame.mixer.music.set_volume(0.5)

# color data
white = (255, 255, 255)
black = (0, 0, 0)
green = (0,255,0)
red = (255,0,0)
bg_color = (231, 213, 189)
boarder_color = (124, 81, 47)
winner_color = (24, 42, 66)
health_font = pygame.font.SysFont('comicsans', multiplier//2)
winner_font = pygame.font.SysFont('comicsans', int(multiplier*1.5))
bgd_music1 = pygame.mixer.Sound(os.path.join('game_data', 'bgm1.mp3'))
bgd_music2 = pygame.mixer.Sound(os.path.join('game_data', 'bgm2.mp3'))
bgd_music3 = pygame.mixer.Sound(os.path.join('game_data', 'bgm3.mp3'))
gun_shot = pygame.mixer.Sound(os.path.join('game_data', 'gun_shot.mp3'))
hurt_man = pygame.mixer.Sound(os.path.join('game_data', 'hurt_man.mp3'))
game_won = pygame.mixer.Sound(os.path.join('game_data', 'game_won.mp3'))

# scales
win_scale=(win_w,win_h)
man_scale = (5*multiplier/4,6*multiplier/4)
gun_scale = (4*multiplier/5, 5*multiplier/5)
fps = 60

# velocities


# user define pygame event
b_hit_r = pygame.USEREVENT + 1
b_hit_l = pygame.USEREVENT + 2
ult_hit_r = pygame.USEREVENT + 3
ult_hit_l = pygame.USEREVENT + 4

# bullets data
bullets_l = []
bullets_r = []
ults_r=[]
ults_l=[]

# load img
# pygame.transform has many inbuilt functions for img manipulation
bg_img = pygame.image.load(os.path.join('game_data', 'bg_img2.jpg'))
bg_img = pygame.transform.scale(bg_img, win_scale)
man_l = pygame.image.load(os.path.join('game_data', 'man1.jpg'))
man_l = pygame.transform.scale(man_l, man_scale)
man_r = pygame.image.load(os.path.join('game_data', 'man2.jpg'))
man_r = pygame.transform.flip(pygame.transform.scale(man_r, man_scale), True, False)
gun_l = pygame.image.load(os.path.join('game_data', 'gun1.png'))
gun_l = pygame.transform.scale(gun_l, gun_scale)
gun_r = pygame.image.load(os.path.join('game_data', 'gun2.png'))
gun_r = pygame.transform.flip(pygame.transform.scale(gun_r, gun_scale), True, False)


def man_r_movement(key_pressed, man_r):
    if key_pressed[pygame.K_UP] and man_r.y - vel > 0:
        man_r.y -= vel
    if key_pressed[pygame.K_DOWN] and man_r.y + vel < win_h - man_r.h:
        man_r.y += vel
    if key_pressed[pygame.K_RIGHT] and man_r.x + vel < win_w - man_r.w:
        man_r.x += vel
    if key_pressed[pygame.K_LEFT] and man_r.x - vel > win_w / 2 + 20:
        man_r.x -= vel


def man_l_movement(key_pressed, man_l):
    if key_pressed[pygame.K_w] and man_l.y - vel > 0:
        man_l.y -= vel
    if key_pressed[pygame.K_s] and man_l.y + vel < win_h - man_l.h:
        man_l.y += vel
    if key_pressed[pygame.K_d] and man_l.x + vel < win_w / 2 - man_l.w - 20:
        man_l.x += vel
    if key_pressed[pygame.K_a] and man_l.x - vel > 0:
        man_l.x -= vel


def draw_display(man_lr, man_rr, bullets_l, bullets_r, health_r, health_l, ult_l,ult_r):
    win.blit(bg_img, (0,0))
    pygame.draw.line(win, boarder_color, (win_w / 2 - 20, 0), (win_w / 2 - 20, win_h))
    pygame.draw.line(win, boarder_color, (win_w / 2 + 20, 0), (win_w / 2 + 20, win_h))

    # man appears
    win.blit(man_l, (man_lr.x, man_lr.y))
    win.blit(man_r, (man_rr.x, man_rr.y))
    # get guns
    win.blit(gun_l, (man_lr.x + man_scale[0]/5, man_lr.y +man_scale[1]*0.8))
    win.blit(gun_r, (man_rr.x+man_scale[0]/5, man_rr.y + man_scale[1]*0.8))

    health_l_text = health_font.render('Health :' + str(health_l), 1, black)
    win.blit(health_l_text, (8, 8))
    health_r_text = health_font.render('Health :' + str(health_r), 1, black)
    win.blit(health_r_text, (win_w - health_r_text.get_width() - 8, 8))


    corner_r=3
    width = 2
    pygame.draw.rect(win, black, (10, win_h - 20,80, 15), width, -1, corner_r,corner_r,corner_r,corner_r)
    pygame.draw.rect(win, black, ( win_w - 200, win_h - 20,80, 15), width, -1,corner_r,corner_r,corner_r,corner_r)
    pygame.draw.rect(win, green, (10+width, win_h - 20+width, (80-2*width)*ult_l*0.1, 15-2*width), 0, -1, corner_r, corner_r, corner_r, corner_r)
    pygame.draw.rect(win, green, (win_w - 200+width, win_h - 20+width, (80-2*width)*ult_r*0.1, 15-2*width), 0, -1, corner_r, corner_r, corner_r, corner_r)

    # fire bullet if triggered
    for bullet in bullets_l:
        pygame.draw.rect(win, black, bullet)
    for bullet in bullets_r:
        pygame.draw.rect(win, black, bullet)
    for ult in ults_r:
        pygame.draw.rect(win, white, ult)
    for ult in ults_l:
        pygame.draw.rect(win, white, ult)

    pygame.display.update()


def post_game_screen(s, bgm):
    text = ''
    if s == 'r':
        text = "Right cowboy wins!"
    if s == 'l':
        text = "Left cowboy wins!"
    bgm.stop()
    game_won.play()
    winner_text = health_font.render(text, 1, winner_color)
    win.blit(winner_text, (win_w / 2 - winner_text.get_width() / 2, win_h / 2 - winner_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(7000)



def game_initialize():
    clock = pygame.time.Clock()
    # rectangle for storing and manipulating position of men
    man_r = pygame.Rect(win_w-man_scale[0]-10, win_h/2, man_scale[0], man_scale[1])
    man_l = pygame.Rect(10, win_h/2, man_scale[0], man_scale[1])
    run = True
    health_r, health_l = max_health, max_health
    bgm = random.choice([bgd_music1, bgd_music2, bgd_music3])
    bgm.play()
    ult_r=0.0
    ult_l=0.0
    return clock, run, man_r, man_l, health_r, health_l, ult_l,ult_r, bgm


def action(man_l, man_r, bullets_l, bullets_r):
    for bullet in bullets_l:
        bullet.x += bullet_vel
        if man_r.colliderect(bullet):
            pygame.event.post(pygame.event.Event(b_hit_r))
            bullets_l.remove(bullet)
        elif bullet.x > win_w:
            bullets_l.remove(bullet)
    for bullet in bullets_r:
        bullet.x -= bullet_vel
        if man_l.colliderect(bullet):
            pygame.event.post(pygame.event.Event(b_hit_l))
            bullets_r.remove(bullet)
        elif bullet.x < 0:
            bullets_r.remove(bullet)
    for ult in ults_r:
        ult.x -= ult_vel
        if man_l.colliderect(ult):
            pygame.event.post(pygame.event.Event(ult_hit_l))
            ults_r.remove(ult)
        elif ult.x < 0:
            ults_r.remove(ult)
    for ult in ults_l:
        ult.x += ult_vel
        if man_r.colliderect(ult):
            pygame.event.post(pygame.event.Event(ult_hit_r))
            ults_l.remove(ult)
        elif ult.x >win_w:
            ults_l.remove(ult)

def update_ults(ult_r,ult_l): #0.05
    ult_increase_rate = 0.2
    if ult_r < 10:
        ult_r += ult_increase_rate
    if ult_l < 10:
        ult_l += ult_increase_rate
    return ult_r,ult_l

def main():  # main game login will be here
    clock, run, man_r, man_l, health_r, health_l, ult_r, ult_l, bgm = game_initialize()
    last_recd_time = 0
    while run:
        # fps setting
        current_time = pygame.time.get_ticks()
        clock.tick(fps)
        # pygame.event
        for event in pygame.event.get():
            if (current_time/1000)!=last_recd_time:
                ult_r,ult_l = update_ults(ult_r, ult_l)
                last_recd_time=current_time/1000
            if event.type == pygame.QUIT:
                run = False
                # pygame.quit
            if event.type == pygame.KEYDOWN:
                # print('#####')
                if (event.key == pygame.K_q ) and len(bullets_l) < max_bullets:
                    bullet = pygame.Rect(man_l.x + man_l.w, man_l.y + man_l.h - 5, 10, 4)
                    gun_shot.play()
                    bullets_l.append(bullet)
                if (event.key == pygame.K_RCTRL) and len(bullets_r) < max_bullets:
                    bullet = pygame.Rect(man_r.x, man_r.y + man_r.h - 5, 10, 4)
                    gun_shot.play()
                    bullets_r.append(bullet)
                if (event.key == pygame.K_e) and ult_l >= 10:
                    ult_bullet = pygame.Rect(man_l.x + man_l.w, man_l.y + man_l.h - 5, 10, 4)
                    gun_shot.play()
                    ults_l.append(ult_bullet)
                    ult_l=0
                if (event.key == pygame.K_SLASH) and ult_r >= 10:
                    ult_bullet = pygame.Rect(man_r.x, man_r.y + man_r.h - 5, 10, 4)
                    gun_shot.play()
                    ults_r.append(ult_bullet)
                    ult_r=0

            if event.type == b_hit_l:
                health_l -= 1
                hurt_man.play()
                ult_l=0
            if event.type == b_hit_r:
                health_r -= 1
                hurt_man.play()
                ult_r = 0
            if event.type == ult_hit_r:
                health_r -= 3
                hurt_man.play()
                hurt_man.play()
                ult_r = 0
            if event.type == ult_hit_l:
                health_l -= 3
                hurt_man.play()
                hurt_man.play()
                ult_l = 0

        if health_r <= 0:
            draw_display(man_l, man_r, bullets_l, bullets_r, health_r, health_l, ult_l,ult_r)
            post_game_screen('r', bgm)
            break
        elif health_l <= 0:
            draw_display(man_l, man_r, bullets_l, bullets_r, health_r, health_l,ult_l,ult_r)
            post_game_screen('l', bgm)
            break

        # make display white, update
        key_pressed = pygame.key.get_pressed()
        man_r_movement(key_pressed, man_r)
        man_l_movement(key_pressed, man_l)
        action(man_l, man_r, bullets_l, bullets_r)
        #print(ult_l,ult_r)
        draw_display(man_l, man_r, bullets_l, bullets_r, health_r, health_l, ult_l,ult_r)

    pygame.quit()
    # main() if u want to restart


# if one runs this file (pygame_learning.py) then this is true
if __name__ == "__main__":
    main()

# todo
# remove bg from man img
# choose man and gun, pregame screen
# post game screen with butcher/cowboy/don/gangster dialogs
# change bg img


#enter name
#login and history , leaderboard
# ultimate bullet
#make img bg remover


#ult not updating with time but keys pressed