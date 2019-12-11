#after doing the sorting of the dirts in the list
#matrix 4x4
import random
from personal_utils import *
import matplotlib.pyplot as plt

m = 15
n = 15
# random.seed(518)
grid = [(random.choice([0, 0, 0, 0, 0, 1]), i, j) for j in range(m) for i in range(n)]


initial = (0,0)
explored = [initial]
old_explored = greedy(grid, initial, explored)


plt.plot(*zip(*old_explored), alpha = 0.5)
plt.scatter(*zip(*old_explored))
plt.scatter(initial[0], initial[1])
plt.xticks(range(m))
plt.yticks(range(n))
plt.grid()
plt.show()
#plt.title('OLD')
#print(old_explored)
new_explored = two_opt_swap(old_explored)
plt.plot(*zip(*new_explored), linestyle = '--')
plt.scatter(*zip(*new_explored))
#plt.title('NEW')
plt.scatter(initial[0], initial[1])
plt.xticks(range(m))
plt.yticks(range(n))
plt.grid()
plt.show()
#print(new_explored)