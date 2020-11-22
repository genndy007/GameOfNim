import pygame

# Screen params
WIN_WIDTH = 700
WIN_HEIGHT = 600
FPS = 60

# Drawing things offsets
OFFSET_X = 100
OFFSET_Y = 50
THING_WIDTH = 40
OFF_BETW_THINGS = 20


# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

# Gameplay basics
###############
################
TURN_HUMAN = 1
TURN_COMPUTER = 2
INITIAL_PILES = [3,5,7]
#########################
######################


# initialise my precious pygame
pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Game of Nim - game of full info")
clock = pygame.time.Clock()


# Bot mechanics
##################################
################################

def xor_array(arr):
    result = 0
    for el in arr:
        result ^= el

    return result





def trying_to_make_perfect_move():
    for i in range(len(INITIAL_PILES)):   # go through every pile
        pile = INITIAL_PILES[i]         # get the pile
        if pile == 0:           # if it's empty then we
            continue            # have nothing to pull out
        
        # this is gonna be a move
        for remove in range(1, pile+1):
            move = []     # check every variant of take
            result = pile - remove   # this is gonna be result
            
            for j in range(len(INITIAL_PILES)):  # fulfill a move
                if i == j:
                    move.append(result)
                else:
                    move.append(INITIAL_PILES[j])

            # check if move is excellent to a strategy
            # it's what we need
            if xor_array(move) == 0:
                return move


def check_one_pile_left():
    zeros = 0
    for pile in INITIAL_PILES:
        if pile == 0:
            zeros += 1

    if zeros == 2:
        return True

    return False
###################################
#################################
##################




# Thing class
#######################
class Thing:
    def __init__(self, x, y, width, height, pile_number, color=GREEN):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pile_number = pile_number


    def draw(self, scr, outline=BLACK):
        if outline:
            pygame.draw.rect(scr, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(scr, self.color, (self.x, self.y, self.width, self.height), 0)


    def isOver(self, pos):
        mouse_x = pos[0]
        mouse_y = pos[1]

        if mouse_x > self.x and mouse_x < self.x + self.width:
            if mouse_y > self.y and mouse_y < self.y + self.height:
                return True

        return False


##########################
##########################
##########################

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



def show_fullscreen_text(txt):
    font = pygame.font.Font('MenuFont.ttf', 40)
    text = font.render(txt, 1, RED)
    screen.blit(screen, (300, 300))


    
# main game loop
def game():
    # Who's turn at start
    TURN = TURN_HUMAN
    
    txt_winner = 'You win'
    button_submission = Thing(250, 525, 200, 50, None, color=RED)
    running = True
    things = generate_things()
    turn_done = False
    game_over = False
    while running:
        print(INITIAL_PILES)

        screen.fill(WHITE) 

        draw_things(things)
        button_submission.draw(screen)


        if TURN == TURN_COMPUTER:
            one_pile = check_one_pile_left()
            if one_pile:
                things = []
                txt_winner = 'You lost'
                game_over = True
                continue    # THIS MIGHT BREAK
                
            move = trying_to_make_perfect_move()

            for i in range(len(INITIAL_PILES)):
                if move[i] != INITIAL_PILES[i]:
                    times_deleting = INITIAL_PILES[i] - move[i]
                    for i in range(times_deleting):
                        things[i].pop()



            INITIAL_PILES = move
            TURN = TURN_HUMAN
            

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Let normally quit
                running = False

            if TURN == TURN_HUMAN:
                if event.type == pygame.MOUSEBUTTONDOWN:  # if pressed
                    lmb, mmb, rmb = pygame.mouse.get_pressed()
                    x, y = event.pos

                    # Here will be button of submission usage
                    if turn_done and button_submission.isOver((x,y)):
                        TURN = TURN_COMPUTER

                    for i in range(len(things)):   # check all things if pressed on
                        pile = things[i]
                        for j in range(len(pile)):
                            t = pile[j]
                            if t.isOver((x,y)):
                                turn_done = True
                                INITIAL_PILES[i] -= 1
                                pile.remove(t)
                                break


        

        clock.tick(FPS)
        # print(TURN)
        pygame.display.flip()


    


game()

