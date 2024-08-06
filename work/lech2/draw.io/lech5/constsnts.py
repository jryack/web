import random

HEADS = 1
TAILS = 2
tOSSER = 10

def tosses_coin() :
    for toss in range(tOSSER):

        if random.randint(HEADS, TAILS) == HEADS:
            print('HEAD')
        else:
            print('TAILS')
tosses_coin()