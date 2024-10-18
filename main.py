from pygame import *

from spriteClass import GameSprite, Player

''' colors '''
background = (200, 255, 255)

window = display.set_mode((700, 500))
window.fill(background)

clock = time.Clock()

''' creating objects '''
platform_left = Player(player_image='img/platform.png', player_x=5, player_y=200, player_speed=4, wight=150, height=150) 
platform_right = Player(player_image='img/platform.png', player_x=535, player_y=200, player_speed=4, wight=150, height=150)
ball = GameSprite(player_image='img/tenis_ball.png', player_x=200, player_y=200, player_speed=4, wight=50, height=50)


''' variables '''
game = True

'''' game loop '''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    platform_left.reset(window_object=window)
    platform_right.reset(window_object=window)
    ball.reset(window_object=window)

    display.update()
    clock.tick(60)
