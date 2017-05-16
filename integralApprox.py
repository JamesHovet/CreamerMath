# create a program that finds Riemann sums given a function, limits of integration, and number of subintervals. Should output LHS, RHS, Midpoint sums, and trap sums

import functools

#define the function we want to use, in this case, x^2
def f(x):
    return pow(x,2)

lower = 0
upper = 3
intervals = 5000

# calculate dt: the difference between the upper and lower bound divided by the number of intervals
dt = (abs(upper - lower))/intervals

# get the x value for equally spaced points along the range.
xs = [x * dt for x in range(intervals)]

#for each of the above calculated inputs for the function, calculate that output and multiply it by dt
LHS = 0
RHS = 0
MDPT = 0
TRAP = 0
for i in xs:
    LHS += f(i) * dt

    RHS += f(i + dt) * dt

    MDPT += f(i + (dt/2)) * dt

    TRAP += ((f(i) + f(i + dt))/2) * dt
