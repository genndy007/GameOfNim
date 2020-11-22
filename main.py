import pygame
from mech import trying_to_make_perfect_move
from const import INITIAL_PILES, TURN_HUMAN, TURN_COMPUTER
from thing import Thing

# Screen params
WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 60

# Drawing things offsets
OFFSET_X = 100
OFFSET_Y = 100
THING_WIDTH = 40
OFF_BETW_THINGS = 20

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)


# initialise my precious pygame
pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Game of Nim - game of full info")
clock = pygame.time.Clock()

# create array of Thing at start of game
def generate_things():
    things = []
    offx = OFFSET_X
    offy = OFFSET_Y
    for amount in INITIAL_PILES:
        things_pile = []
        for i in range(amount):
            t = Thing(offx, offy, THING_WIDTH, THING_WIDTH)
            things_pile.append(t)
            offy += OFF_BETW_THINGS + THING_WIDTH

        things.append(things_pile)
        offx += 200
        offy = OFFSET_Y
    
    return things


# draw all things on screen
def draw_things(things):
    for pile in things:
        for t in pile:
            t.draw(screen)
    
    
# main game loop
def game():
    running = True
    things = generate_things()
    while running:
        screen.fill(WHITE)
        draw_things(things)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)
        pygame.display.flip()


game()