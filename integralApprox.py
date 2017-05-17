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

#not efficent, shows the esssence of what is going on pretty well (14 ms per loop on 5000 intervals)
def v1():
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
    return (LHS, RHS, MDPT, TRAP)

#more efficent, less readable (4.44 ms per loop on 5000 intervals)
def v2():

    xs = [x * dt for x in range(intervals + 1)]

    ys = [f(x) * dt for x in xs]

    LHS = sum(ys[:-1])
    RHS = LHS - ys[0] + ys[-1]
    TRAP = (LHS + RHS)/2

    MDPT = sum([f(x + (dt/2)) * dt for x in xs[:-1]])

    return (LHS, RHS, MDPT, TRAP)

#an even more efficent way would be to use map and reduce
