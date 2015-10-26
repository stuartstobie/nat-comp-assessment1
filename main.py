# imports
from random import randint
from random import uniform
from statistics import mean
from statistics import stdev
# setup grid: grid[x][y] => grid[0][0]=1, grid[0][1]=4, grid[0][2]=7...
grid = [[y*3+x+1 for y in range(3)] for x in range(3)]
# probabilities to move to corresponding section of grid in task 2.
prob = [[(y+1)/18 for y in range(3)] for x in range(3)]

# returns object to store probabilities in.
def prob_obj():
    return { 1: [], 3: [], 9: [] }

# find the probabity of acceptance; uses metropolis algorithm.
def acceptance(x, y, new_x, new_y):
    if new_x < 0 or new_x > 2:
        return 0
    if new_y < 0 or new_y > 2:
        return 0
    probability = prob[new_x][new_y] / prob[x][y]
    if probability >= 1:
        return 1
    return probability

# decide where to attempt to transition
def move(x, y):
    new_x = x
    new_y = y
    dir = randint(0,3)
    if dir == 0:
        new_y += 1 # North
    if dir == 1:
        new_x += 1 # East
    if dir == 2:
        new_y -= 1 # South
    if dir == 3:
        new_x -= 1 # West
    accept = acceptance(x, y, new_x, new_y)
    if accept == 0:
        return [x,y]
    if accept == 1:
        return [new_x,new_y]
    if uniform(0.0, 1.0) <= accept:
        return [new_x,new_y]
    else:
        return [x,y]

def calc_prob(n, positions):
    return positions.count(n) / len(positions)

def mean_and_std_dev(numbers):
    return [mean(numbers), stdev(numbers)]

def pretty_print(probabilities):
    for i in range(3):
        n = 3**i # looks at numbers 1, 3 & 9
        print('Probability of ending in ' + str(n) + ': ' +
            str(probabilities[n][0]) + ' ± ' + str(probabilities[n][1]))

def task3():
    runs = 100 # repeats in order to find mean and standard deviation
    steps = 3 # time steps
    repeats = 10000
    probabilities = prob_obj()
    for r in range(runs):
        end_positions = []
        for repeat in range(repeats):
            pos = [0,0] # start at 1
            for s in range(steps):
                pos = move(pos[0], pos[1])
            end_positions.append(grid[pos[0]][pos[1]])
        for i in range(3):
            n = 3**i # looks at numbers 1, 3 & 9
            probabilities[n].append(calc_prob(n, end_positions))
    for i in range(3):
        n = 3**i
        probabilities[n] = mean_and_std_dev(probabilities[n])
    print('Task 3')
    pretty_print(probabilities)

def task4():
    runs = 100 # repeats in order to find mean and standard deviation
    steps = 1000000 # time steps
    rec = 1000 # number of time steps to take between recording position
    probabilities = prob_obj()
    for r in range(runs):
        rec_positions = []
        pos = [0,0] # start at 1
        for s in range(steps):
            pos = move(pos[0], pos[1])
            if s > 0 and (s+1)%rec == 0:
                rec_positions.append(grid[pos[0]][pos[1]])
        for i in range(3):
            n = 3**i # looks at numbers 1, 3 & 9
            probabilities[n].append(calc_prob(n, rec_positions))
    for i in range(3):
        n = 3**i
        probabilities[n] = mean_and_std_dev(probabilities[n])
    print('Task 4')
    pretty_print(probabilities)

task3()
task4()
