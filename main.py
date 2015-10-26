from random import randint
from random import uniform
# setup grid: grid[x][y] => grid[0][0]=1, grid[0][1]=4, grid[0][2]=7...
grid = [[y*3+x+1 for y in range(3)] for x in range(3)]
# probabilities to move to corresponding section of grid in task 2.
prob = [[(y+1)/18 for y in range(3)] for x in range(3)]

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

# choose either north, east, sout or west
def direction():
    dir = randint(0,3)
    if dir == 0:
        return 'N'
    elif dir == 1:
        return 'E'
    elif dir == 2:
        return 'S'
    else:
        return 'W'

# decide where to transition to
def move(x, y):
    new_x = x
    new_y = y
    dir = direction()
    if dir == 'N':
        new_y += 1
    if dir == 'E':
        new_x += 1
    if dir == 'S':
        new_y -= 1
    if dir == 'W':
        new_x -= 1
    accept = acceptance(x, y, new_x, new_y)
    if accept == 0:
        return [x,y]
    if accept == 1:
        return [new_x,new_y]
    if uniform(0.0, 1.0) <= accept:
        return [new_x,new_y]
    else:
        return [x,y]

def main():
    moves = int(input('How many time steps would you like to use? '))
    repeats = int(input('How many repeats would you like to perform? '))
    running = input('Would you like to calculate probabilities during each run? (Y or N) ')
    running_steps = 0
    if running == 'Y' or running == 'y':
        running_steps = int(input('How many time steps should be done before the position is recorded? '))
    for i in range(repeats):
        pos = [0,0] # start at 1
        run_results = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            'total': 0
        }
        for j in range(moves):
            pos = move(pos[0], pos[1])
            if j > 0 and running_steps > 0 and (j+1)%running_steps == 0:
                run_results[grid[pos[0]][pos[1]]] += 1
                run_results['total'] += 1
        if running_steps == 0:
            run_results[grid[pos[0]][pos[1]]] += 1
            run_results['total'] += 1
        print(run_results)

main()
