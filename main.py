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
pygame.display.set_caption("Classical Nim game")
clock = pygame.time.Clock()


# Bot mechanics
##################################
################################

def xor_array(arr):
    result = 0
    for el in arr:
        result ^= el

    return result





def trying_to_make_perfect_move(piles):
    for i in range(len(piles)):   # go through every pile
        pile = piles[i]         # get the pile
        if pile == 0:           # if it's empty then we
            continue            # have nothing to pull out
        
        # this is gonna be a move
        for remove in range(1, pile+1):
            move = []     # check every variant of take
            result = pile - remove   # this is gonna be result
            
            for j in range(len(piles)):  # fulfill a move
                if i == j:
                    move.append(result)
                else:
                    move.append(piles[j])

            # check if move is excellent to a strategy
            # it's what we need
            if xor_array(move) == 0:
                return move


def make_typical_move(piles):
    for i in range(len(piles)):
        pile = piles[i]
        if pile == 0:
            continue

        piles[i] -= 1
        break
    
    return piles
    


def check_one_pile_left(piles):
    zeros = 0
    for pile in piles:
        if pile == 0:
            zeros += 1

    if zeros == 2:
        return True

    return False



def find_index_where_not_zero(piles):
    for i in range(len(piles)):
        if piles[i] != 0:
            return i



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




# Button class
##########################
class Button:
    def __init__(self, x, y, width, height, color=GREEN, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, scr, outline=None):
        if outline:
            pygame.draw.rect(scr, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(scr, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.Font('MenuFont.ttf', 20)
            text = font.render(self.text, 1, BLACK)
            scr.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):   # Here we take mouse position and compare it
        mouse_x = pos[0]
        mouse_y = pos[1]
        if mouse_x > self.x and mouse_x < self.x + self.width:
            if mouse_y > self.y and mouse_y < self.y + self.height:
                return True
        
        return False

##########################

# create array of Thing at start of game
def generate_things(piles):
    things = []
    offx = OFFSET_X
    offy = OFFSET_Y
    for i in range(len(piles)):
        amount = piles[i]
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
    screen.blit(text, (300, 300))


    
# main game loop
def game():
    ############# HELP SHOWING
    # Application shows rules of game at start
    rule_font = pygame.font.Font('MenuFont.ttf', 28)
    rules = "Nim is a game where players take things that are placed in 3 piles.\n\
At one turn, player can take any number of things of only one pile.\n\
Submit your choice with pressing red button at screen bottom.\n\
The winner is who takes the last thing.\n\
I wish you luck, but opponent plays ultimate winning strategy!"
    lines = rules.split('\n')
    showing_rules = True
    button_ok = Button(250, 400, 200, 50, text="Ok. Bring it on!")
    while showing_rules:
        screen.fill(WHITE)
        button_ok.draw(screen, outline=BLACK)
        off_lines = 0
        for line in lines:
            rule_text = rule_font.render(line, 1, BLACK)
            screen.blit(rule_text, (50, 100+off_lines))
            off_lines += 40

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Let normally quit
                showing_rules = False
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                lmb, mmb, rmb = pygame.mouse.get_pressed()
                x, y = event.pos

                if button_ok.isOver((x,y)):
                    showing_rules = False


        clock.tick(FPS)
        pygame.display.flip() 

    ######## TURN CHOICE
    # Who's turn at start
    TURN = TURN_HUMAN
    turn_choose = True
    button_human = Button(250, 200, 200, 50, text="Human first")
    button_comp = Button(250, 400, 200, 50, text="Computer first")
    while turn_choose:
        screen.fill(WHITE)

        button_human.draw(screen, outline=BLACK)
        button_comp.draw(screen, outline=BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Let normally quit
                turn_choose = False
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                lmb, mmb, rmb = pygame.mouse.get_pressed()
                x, y = event.pos

                if button_human.isOver((x,y)):
                    TURN = TURN_HUMAN
                    turn_choose = False
                if button_comp.isOver((x,y)):
                    TURN = TURN_COMPUTER
                    turn_choose = False


        clock.tick(FPS)
        pygame.display.flip()    


    ############ MAIN GAME
    piles = [3,5,7]
    txt_winner = 'You win'
    button_submission = Thing(250, 525, 200, 50, None, color=RED)
    running = True
    things = generate_things(piles)
    turn_done = False
    game_over = False
    human_chose_pile = None
    while running:
        # print(piles)
        # print(TURN)
        # print(things)
        screen.fill(WHITE) 

        draw_things(things)
        button_submission.draw(screen)


        if TURN == TURN_COMPUTER:
            one_pile = check_one_pile_left(piles)
            if one_pile:
                print("One pile")
                idx = find_index_where_not_zero(piles)
                for _ in range(piles[idx]):
                    things[idx].pop()

                piles[idx] = 0
                txt_winner = 'You lost'
                running = False
                game_over = True
                continue    # THIS MIGHT BREAK
                
            move = trying_to_make_perfect_move(piles)
            # print(move)

            if move is not None:
                for i in range(len(piles)):
                    if move[i] != piles[i]:
                        times_deleting = piles[i] - move[i]
                        for j in range(times_deleting):
                            things[i].pop()

                piles = move
            else:
                bad_move = make_typical_move(piles)    # do a bad move
                for i in range(len(piles)):
                    if bad_move[i] != piles[i]:
                        things[i].pop()


            TURN = TURN_HUMAN   # end turn and give it to human
            human_chose_pile = None

        
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
                                if human_chose_pile is None:  # here is choice prohibition
                                    human_chose_pile = i
                                    turn_done = True
                                    piles[i] -= 1
                                    pile.remove(t)
                                    break
                                elif human_chose_pile == i:
                                    piles[i] -= 1
                                    pile.remove(t)
                                    break


        

        clock.tick(FPS)
        # print(TURN)
        pygame.display.flip()

    while game_over:
        screen.fill(WHITE)
        show_fullscreen_text(txt_winner)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Let normally quit
                game_over = False


        clock.tick(FPS)
        pygame.display.flip()


    


game()

