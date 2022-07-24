import pygame
import os
import random

pygame.font.init()
pygame.mixer.init()
# 1st thing is to create window aka surface

win_h = 500
win_w = 800

win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("West_gunfighter_game_solo")
pygame.mixer.music.set_volume(0.5)

# color data
white = (255, 255, 255)
black = (0, 0, 0)
bg_color = (231, 213, 189)
boarder_color = (124, 81, 47)
winner_color = (24, 42, 66)
health_font = pygame.font.SysFont('comicsans', 32)
winner_font = pygame.font.SysFont('comicsans', 80)
bgd_music1 = pygame.mixer.Sound(os.path.join('game_data', 'bgm1.mp3'))
bgd_music2 = pygame.mixer.Sound(os.path.join('game_data', 'bgm2.mp3'))
bgd_music3 = pygame.mixer.Sound(os.path.join('game_data', 'bgm3.mp3'))
hurt_man = pygame.mixer.Sound(os.path.join('game_data', 'hurt_man.mp3'))
gun_shot = pygame.mixer.Sound(os.path.join('game_data', 'gun_shot.mp3'))
fireball_start = pygame.mixer.Sound(os.path.join('game_data2', 'fireball_start.mp3'))
fireball_end = pygame.mixer.Sound(os.path.join('game_data2', 'fireball_end.mp3'))

highest_score_won = pygame.mixer.Sound(os.path.join('game_data', 'game_won.mp3'))

# scales
man_scale = (75, 90)
gun_scale = (60, 75)
fb_scale = (60, 75)

fps = 60

# velocities
vel = 2
bullet_vel = 5
fire_ball_vel = 6
acc_per_level=0.03
max_bullets = 5
max_health = 5

# user define pygame event
hit_man = pygame.USEREVENT + 1
hit_fireball = pygame.USEREVENT + 2
hit_wall = pygame.USEREVENT + 3

# bullets data
bullets = []
fire_balls = []
fb_vel_x=[]
fb_vel_y=[]

# load img
# pygame.transform has many inbuilt functions for img manipulation
man_pic = pygame.image.load(os.path.join('game_data', 'man1.jpg'))
man_pic = pygame.transform.flip(pygame.transform.scale(man_pic, man_scale),True,False)
gun_pic = pygame.image.load(os.path.join('game_data', 'gun1.png'))
gun_pic = pygame.transform.flip(pygame.transform.scale(gun_pic, gun_scale),True,False)
fire_ball_pic = pygame.image.load(os.path.join('game_data2', 'fire_ball.png'))
fire_ball_pic = pygame.transform.scale(fire_ball_pic, fb_scale)



def game_initialize():
    clock = pygame.time.Clock()

    # rectangle for storing and manipulating position of men
    man = pygame.Rect(win_w-100, win_h / 2, man_scale[0], man_scale[1])
    fireball = pygame.Rect(30, win_h / 2, fb_scale[0], fb_scale[1])

    run = True
    health = max_health
    level = 0
    bgm = random.choice([bgd_music1, bgd_music2, bgd_music3])
    # bgm.play()
    return clock, run, man, fireball, health, bgm, level

def remove_fb(hitfb):
    fire_balls.remove(fire_balls[hitfb])
    fb_vel_x.remove(fb_vel_x[hitfb])
    fb_vel_y.remove(fb_vel_y[hitfb])


def fireball_fire():
    h = random.randint(5, win_h - fire_ball_pic.get_height())
    w = 30
    fb = pygame.Rect(w, h, fb_scale[0], fb_scale[1])
    fire_balls.append(fb)
    new_x_vel = random.randint(5,fire_ball_vel*10)/10
    fb_vel_x.append(new_x_vel)
    fb_vel_y.append(fire_ball_vel-new_x_vel)


def man_movement(key_pressed, man):
    if (key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]) and man.y - vel > 0:
        man.y -= vel
    if (key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]) and man.y + vel < win_h - man.h:
        man.y += vel
    if (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and man.x + vel < win_w - man.w:
        man.x += vel
    if (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and man.x - vel > 0:
        man.x -= vel


def fireball_movement(level):
    for i in range(len(fire_balls)):
        fire_balls[i].x += (fb_vel_x[i]+acc_per_level*level)
        fire_balls[i].y += (fb_vel_y[i]+acc_per_level*level)


def draw_display(man_lr, bullets_l, health_r, game_level, fire_balls):
    win.fill(bg_color)
    # man appears
    win.blit(man_pic, (man_lr.x, man_lr.y))
    # get guns
    # if man_lr.x<win_w/2:
    #    gun_pic=pygame.transform.flip(gun_pic,True,False)
    win.blit(gun_pic, (man_lr.x + 10, man_lr.y + 60))
    # fire bullet if triggered
    game_level_text = health_font.render('Level :' + str(game_level), True, black)
    win.blit(game_level_text, (8, 8))
    health_r_text = health_font.render('Health :' + str(health_r), True, black)
    win.blit(health_r_text, (win_w - health_r_text.get_width() - 8, 8))

    for bullet in bullets_l:
        pygame.draw.rect(win, black, bullet)
    for fb in fire_balls:
        win.blit(fire_ball_pic, (fb.x, fb.y))
    pygame.display.update()


def post_game_screen(level, bgm):
    text = 'Game Over'
    bgm.stop()
    winner_text = health_font.render(text, True, winner_color)
    win.blit(winner_text, (win_w / 2 - winner_text.get_width() / 2, win_h / 2 - winner_text.get_height()))
    winner_text = health_font.render('You reached level ' + str(level), True, winner_color)
    win.blit(winner_text, (win_w / 2 - winner_text.get_width() / 2, win_h / 2 + winner_text.get_height()))
    pygame.display.update()
    pygame.time.delay(4000)




def action(man_l, fire_ball, bullets_l,hitwall,hitfb, hitman):
    for bullet in bullets_l:
        for i in range(len(fire_ball)):
            if bullet.colliderect(fire_ball[i]):
                pygame.event.post(pygame.event.Event(hit_fireball))
                hitfb=i
                bullets_l.remove(bullet)
                fire_ball.remove(fire_ball[i])
                fireball_fire()
        bullet.x -= bullet_vel
        if bullet.x <0:
            bullets_l.remove(bullet)

    for i in range(len(fire_ball)):
        if fire_ball[i].colliderect(man_l):
            pygame.event.post(pygame.event.Event(hit_man))
            fire_ball.remove(fire_ball[i])
            hitman=i
        elif fire_ball[i].y < 0 or fire_ball[i].y > win_h - fire_ball[i][3]:
            pygame.event.post(pygame.event.Event(hit_wall))
            hitwall=i
        elif fire_ball[i].x > win_w:
            fire_ball.remove(fire_ball[i])

        return hitfb, hitwall, hitman


def main():  # main game login will be here
    clock, run, man,fireball, health, bgm, level = game_initialize()
    hitwall=-1
    hitfb = -1
    hitman =-1
    while run:
        # fps setting
        clock.tick(fps)
        # pygame.event:?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # pygame.quit
            if event.type == pygame.KEYDOWN:
                # print('#####')
                if event.key == pygame.K_SPACE and len(bullets) < max_bullets:
                    bullet = pygame.Rect(man.x , man.y + man.h - 5, 10, 4)
                    #gun_shot.play()
                    bullets.append(bullet)

            if event.type == hit_man:
                health -= 1
                #hurt_man.play()
                hitman=-1
            if event.type == hit_fireball and hitfb>-1:
                level += 1
                remove_fb(hitfb)
                hitfb=-1
                #fireball_end.play()
            if event.type == hit_wall and hitwall>-1:
                fb_vel_y[hitwall] = -fb_vel_y[hitwall]
                hitwall=-1
        if len(fire_balls)<1+level/10:
            fireball_fire()
        if health <= 0:
            draw_display(man, bullets, health, level, fire_balls)
            post_game_screen(level, bgm)
            break
        print("firebalss rn: " + str(len(fire_balls)))
        print(len(bullets))
        # make display white, update
        key_pressed = pygame.key.get_pressed()
        man_movement(key_pressed, man)
        fireball_movement(level)
        hitwall, hitfb, hitman = action(man, fire_balls, bullets,hitwall,hitfb, hitman)
        # print(len(bullets_l), len(bullets_r))
        draw_display(man, bullets, health, level, fire_balls)

    pygame.quit()
    # main() if u want to restart


# if one runs this file (pygame_learning.py) then this is true
if __name__ == "__main__":
    main()

# todo
# multifb independent not working independently
# check random position and random vel initialization of all fb
# check if hit function to man, wall is correct
# hit fb is also  not working prefectly
# vel remove
