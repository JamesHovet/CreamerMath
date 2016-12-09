import math

def p1():
    c = 0
    for i in range(1,1000):
        if i % 3 == 0:
            c += i
        elif i % 5 == 0:
            c += i
    return c

def p1v2(): #takes the same time as above, but uses fewer lines
    c = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            c += i
    return c

FOUR_MILLION = 4000000

def genFib(UpTo):
    f = [1,1] #f is the list of fib numbers, started with 1 and 1
    a,b = 1,1
    while b < UpTo:
        a = a+b
        b = b+a
        if a < UpTo:
            f.append(a)
        if b < UpTo:
            f.append(b)

    return f

def p2():
    f = genFib(FOUR_MILLION)
    s = 0
    for i in f:
        if i % 2 == 0:
            s+= i

    return s


def numIsPalindrome(n):
    if str(n) == str(n)[::-1]: #fancy shortcut, tests if the number as a string is the same as the number as a string reversed, see "extended slices" in docs: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
        return True
    else:
        return False

def numIsPalindromeOld(n):
    l = len(str(n))
    s = str(n)
    upTo = math.floor(l/2)

    for i in range(upTo):
        if not s[i] == s[-i -1]:
            return False

    return True

def p3():
    top = 0
    for a in range(100,1000):
        for b in range(100,1000):
            if numIsPalindrome(a*b) and a*b > top:
                top = a*b

    return top
