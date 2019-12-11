import numpy as np
import random
import matplotlib.pyplot as plt

def sort_dirt(grid):
    #getting dirt locations
    return [(i[1],i[2]) for i in grid if i[0] == 1]

def dist(start_place,dirts):
    dirt_path = [abs(start_place[0] - i[0]) + abs(start_place[1] - i[1]) for i in dirts]
    next_node = dirts[dirt_path.index(min(dirt_path))]
    return next_node

def greedy(grid, initial_state, explored_nodes):
    dirt_list = sort_dirt(grid)
    while len(dirt_list) != 0:
        initial_state = dist(initial_state,dirt_list)
        dirt_list.remove(initial_state)
        explored_nodes.append(initial_state)
    return explored_nodes

def pairwise_manhattan(l):
    l1x = np.array([i[0] for i in l[:len(l)-1]])
    l1y = np.array([i[1] for i in l[:len(l)-1]])
    l2x = np.array([i[0] for i in l[1:]])
    l2y = np.array([i[1] for i in l[1:]])
    return abs(l2x - l1x) + abs(l2y - l1y)

# def two_opt_swap(explored_nodes):
# 	old_cost = sum(pairwise_manhattan(explored_nodes))
# 	print(old_cost)
# 	new_cost = 0 
# 	counter = 0
# 	while old_cost > new_cost:
# 		if counter > 0:
# 			old_cost = new_cost
# 			counter += 1
# 		nodes_indices = random.sample(range(1, len(explored_nodes)), 2)
# 		explored_nodes[nodes_indices[0]], explored_nodes[nodes_indices[1]] = explored_nodes[nodes_indices[1]], explored_nodes[nodes_indices[0]]
# 		new_cost = sum(pairwise_manhattan(explored_nodes))
# 		if new_cost >= old_cost:
# 			explored_nodes[nodes_indices[0]], explored_nodes[nodes_indices[1]] = explored_nodes[nodes_indices[1]], explored_nodes[nodes_indices[0]]
# 		print(new_cost)
# 	return explored_nodes

def two_opt_swap(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+1, len(route)):
                if j-i == 1:
                    continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if sum(pairwise_manhattan(new_route)) < sum(pairwise_manhattan(best)):
                    best = new_route
                    improved = True
        route = best
    return best