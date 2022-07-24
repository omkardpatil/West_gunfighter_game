import pygame.display

from West_gunfighter_game_multiplayer import *
from West_gunfighter_game_solo import *

win_h_main = 500
win_w_main = 800

font1 = pygame.font.SysFont('comicsans', 32)
font2 = pygame.font.SysFont('comicsans', 80)

win_main = pygame.display.set_mode((win_w_main, win_h_main))
pygame.display.set_caption("West_gunfighter_game")

pygame.font.init()

class button():
    def __init__(self,x,y,text):
        self.text = font1.render(text, True, black)
        self.x=x
        self.y=y

    def get_text_rect(self):
        return self.x-self.text.get_width()/2-10,self.y-self.text.get_height()/2-7.5,self.text.get_width()+20,self.text.get_height()+15

    def draw(self):
        pygame.draw.rect(win_main,black,(self.get_text_rect()),2,1,1,1,1,1)
        win_main.blit(self.text, (self.x-self.text.get_width()/2, self.y-self.text.get_height()/2))


def Draw_window(solo_button, multi_button):
    win_main.fill(bg_color)
    select_game_text = font1.render('Select Game mode', True, black)
    win_main.blit(select_game_text, (win_w_main/2-select_game_text.get_width()/2,win_h_main*2/5-select_game_text.get_height()))
    solo_button.draw()
    multi_button.draw()
    pygame.display.update()


def checkifclicked(solo, multi):
    print(pygame.mouse.get_pressed())
    print(pygame.mouse.get_pos())

def initialize():
    run=True
    clock=pygame.time.Clock()
    solo_button = button(win_w_main / 4, win_h_main/2, 'Solo')
    multi_button = button(win_w_main * 3 / 4, win_h_main/2, 'Multiplayer')
    return run , clock, solo_button, multi_button

def run_game(mouse_pos, solo_button, multi_button):
    solo_rect=solo_button.get_text_rect()
    multi_rect = multi_button.get_text_rect()
    run = False
    if(mouse_pos[0]>solo_rect[0] and mouse_pos[0]<solo_rect[0]+solo_rect[2] and mouse_pos[1]>solo_rect[1] and mouse_pos[1]<solo_rect[1]+solo_rect[3]):
        os.system('python West_gunfighter_game_solo.py')

    elif (mouse_pos[0]>multi_rect[0] and mouse_pos[0]<multi_rect[0]+multi_rect[2] and mouse_pos[1]>multi_rect[1] and mouse_pos[1]<multi_rect[1]+multi_rect[3]):
        os.system('python West_gunfighter_game_multiplayer.py')
    else:
        print("Click on one of two buttons!")
        run =True

    return run

def main():
    run, clock, solo_button, multi_button=initialize()

    while(run):
        Draw_window(solo_button, multi_button)
        # fps setting
        clock.tick(fps)
        # pygame.event:?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

        if (pygame.mouse.get_pressed()==(1,0,0)):
            mouse_pos = pygame.mouse.get_pos()
            run = run_game(mouse_pos, solo_button, multi_button)
            if (run==False):
                pygame.time.delay(3000)


if __name__ == "__main__":
    main()
