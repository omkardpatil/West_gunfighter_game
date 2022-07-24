# West_gunfighter_game

Replicating western classic showdown aka walkdown, it is a 2D, a stratergic, shooting game, made in python from scratch.

The game interface using the pygame library. • Features multiplayer game mode and a endless single player mode with increasing difficulty with score



## To start game:

clone the repo to local dir

run Main.py

Select game mode:

(depending on what you want to play)

Western_gunfight_game_multiplayer or Western_gunfight_game_solo 


![pygame](https://user-images.githubusercontent.com/81369524/180657471-0bc34051-a663-48cf-b69e-828979d23a9e.png)

## Pre rec:

i)Install python
    https://www.python.org/downloads/

ii) Install pygame

    How to Install Pygame on Windows: https://www.youtube.com/watch?v=AdUZA...

    How to Install Pygame on Mac: https://www.youtube.com/watch?v=E-WhA...

## Pygame Basics

I] Initiate window (aka surface)
    
    `win_main = pygame.display.set_mode((win_width, win_height))`
    
II] Displaying window

    `pygame.display.update()
    #You must use this command to see update your windows with any chages done'
    
These two are essential and smallest sufficient code to create a basic pygame window.

## other features:

0) Coordinate system:
    
   Just like turtleSim from CS101:
    
   ![coordinate_system_pygame](https://user-images.githubusercontent.com/81369524/180658400-d3e42008-4102-4257-a397-aad3673dc69a.png)

1) Name window
    
    'pygame.display.set_caption("Name of window")'

2) Draw
    
    `pygame.draw.rect(win_name, color, Rect)`
    
    other available functions: polygon, line, circle, ellipse, arc, etc 

3) img
    
    loading an img
    
    `pic = pygame.image.load(os.path.join('dir', 'image_name.png')`
    
    transformation in pygame!!!
    
    `pic = pygame.transform.scale(pic, scale)`
    
    // other available functions: flip, rotate, thresholding, avg_color etc
    
    `win_name.blit(pic, (x,y))`

4) font
    
    load font
    
    `pygame.font.init()
    
    user_font = pygame.font.SysFont('comicsans', 80) #font name, size'


5) music
    
    loade music
    
    `pygame.mixer.init()`
    
    set volume (for some reason it is not working in the repo)
    
    `pygame.mixer.music.set_volume(0.5)`
    
    `music = pygame.mixer.Sound(os.path.join('repo', 'somng_name.mp3'))
    
    music.play()`

6) Collision detection
    
    for collision between rectangles or one rectangle and other object
    
    pygame provides a beautiful function
    
    `rectangle_1.colliderect(rectangle_2)`
    
     rectangle_2 can be any object


## Game logic developement process

