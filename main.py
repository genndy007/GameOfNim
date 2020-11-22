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

# Who's turn at start
TURN = TURN_HUMAN
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
    for i in range(len(INITIAL_PILES)):
        amount = INITIAL_PILES[i]
        things_pile = []
        for _ in range(amount):
            t = Thing(offx, offy, THING_WIDTH, THING_WIDTH, i)
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
    turn_done = False
    while running:
        screen.fill(WHITE)
        draw_things(things)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Let normally quit
                running = False

            if TURN = TURN_HUMAN:
                if event.type == pygame.MOUSEBUTTONDOWN:  # if pressed
                    lmb, mmb, rmb = pygame.mouse.get_pressed()
                    x, y = event.pos

                    for i in range(len(things)):   # check all things if pressed on
                        pile = things[i]
                        for j in range(len(pile)):
                            t = pile[j]
                            if t.isOver((x,y)):
                                turn_done = True
                                INITIAL_PILES[i] -= 1
                                pile.remove(t)
                                break


                    # Here will be button of submission usage







        clock.tick(FPS)
        pygame.display.flip()


game()

