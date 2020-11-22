from const import TURN_HUMAN, TURN_COMPUTER, INITIAL_PILES


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



# move = trying_to_make_perfect_move()
# print(move)