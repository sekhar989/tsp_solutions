#after doing the sorting of the dirts in the list
#matrix 4x4
import random
from personal_utils import *
import matplotlib.pyplot as plt

def main(n):

    db = {}

    for i in range(1, n+1):
        
        if i%10 == 0:
            print('Building Pattern Number {}'.format(i))

        x = 15
        y = 15
        
        grid = [(random.choice([0, 0, 0, 0, 0, 1]), i, j) for j in range(x) for i in range(y)]

        initial = (random.choice(range(x)),random.choice(range(x)))
        explored = [initial]
        old_explored = greedy(grid, initial, explored)
        new_explored = two_opt_swap(old_explored)

        db[initial] = new_explored

    with open('pattern_db.txt', 'w') as f:
        f.write(str(db))


if  __name__ == '__main__':
    main(500)

