# Source: https://en.wikipedia.org/wiki/Differential_evolution
import random
import math

def DE(f, argn, N, DW, CR, max_iter, min_eps):
    '''
    f           Function to optimise (convention: maximise)
    argn        Number of arguments taken by f
    N           Number of agents. N >= 4
    DW          Differential weight. DW in [0,2]
    CR          Crossover probability. CR in [0,1]
    max_iter    Maximum number of iterations
    min_eps     Minimum epsilon improvement between generations
    '''
    cur_pop = [[random.random() for i in range(argn)] for j in range(N)]
    fitness = [f(cur_pop[i]) for i in range(N)]

    t, eps = 0, min_eps
    while t < max_iter and eps >= min_eps:
        t += 1
        eps = 0
        new_pop = []

        for i in range(N):
            x = cur_pop[i]

            # Generate 3 other different tagents
            while True:
                r3 = random.sample(range(N), 3)
                if i not in r3:
                    [a,b,c] = [cur_pop[r3[0]], cur_pop[r3[1]], cur_pop[r3[2]]]
                    break

            # Hybrid agent z
            z = [a[j] + DW * (b[j] - c[j]) for j in range(argn)]
            z_fitness = f(z)

            # Perform crossover to create y
            rand_index = random.choice(range(N))
            y = [z[j] if random.random() < CR or j == rand_index else x[j] for j in range(argn)]

            # Add to new population
            x_fitness = f(x)
            y_fitness = f(y)
            new_pop.append(y if y_fitness > x_fitness else x)
            fitness[i] = y_fitness if y_fitness > x_fitness else x_fitness
            eps = max(eps, y_fitness - x_fitness)

        cur_pop = new_pop

    print("Terminated with t = {}, eps = {}".format(t, eps))

    # best = [agent, fitness]
    best = max(zip(cur_pop, fitness), key = lambda x: x[1])
    return best

# TEST
def f(args):
    '''
    f(x,y) = -((x+5)^2 + 3 * sqrt(|y+2| + 7))
    Wolfram: http://www.wolframalpha.com/input/?i=max+-((x%2B5)%5E2+%2B+3*sqrt(%7Cy%2B2%7C%2B+7))
    max{-((x+5)^2+3 sqrt(abs(y+2)+7))}
    approx -7.937253933193771771504847260917781277131
    at (x, y) = (-5, -2)
    '''
    return -((args[0] + 5) ** 2 + 3 * math.sqrt(abs(args[1] + 2) + 7))

argn = 2
N = 1000
DW = 1
CR = 0.5
max_iter = 1e3
min_eps = 1e-6
best = DE(f, argn, N, DW, CR, max_iter, min_eps)
print(best)
print(-7.937253933193771771504847260917781277131)
print("Diff = {}".format(-7.937253933193771771504847260917781277131 - best[1]))