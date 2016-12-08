# Write a program that calculates the probability that when 2 six-sided dice are rolled, that the sum of the pips is 8.
import random
NUM_TRIALS = 10000

def v1(): #clunky but works
    c = 0
    for i in range(NUM_TRIALS):
        if random.randint(1, 6) + random.randint(1, 6) == 8:
            c += 1

    return c/NUM_TRIALS
