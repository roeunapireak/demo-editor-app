from pygame import *

from spriteClass import GameSprite

''' colors '''
background = (200, 255, 255)

window = display.set_mode((700, 500))
window.fill(background)

clock = time.Clock()

''' variables '''
game = True

'''' game loop '''
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
