import random
import os

def roll(number: int, dice: int):
    result = 0
    # print(f"Rolling {number}d{dice}", end=": ")
    for d in range(1,number+1):
        r = random.randint(1, dice)
        # if d != number:
            # end='+'
        # else:
            # end='\n'

        # print(r, end=end)
        result += r

    return result

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
