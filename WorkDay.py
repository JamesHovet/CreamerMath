import math
from IsPrime import isPrime

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


def p2OddIndexedTerms():
    f = genFib(FOUR_MILLION)
    s = 0
    for i in range(1,len(f),2):
        s+= i

    return s


def numIsPalindrome(n):
    if str(n) == str(n)[::-1]: #fancy shortcut, tests if the number as a string is the same as the number as a string reversed, see "extended slices" in docs: https://docs.python.org/2/whatsnew/2.3.html#extended-slices
        return True
    else:
        return False

def numIsPalindromeOld(n): # for every letter up to the center, check if it the same as the letter opposite from it
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

#give prime factorization of any positive integer and reject non-integers



def p4(n): #super function for the primeFactorize function, gives it the namespace to play in
    factors = []
    primeFactorize(n, factors)
    return factors


def primeFactorize(n,factors): #this is recursive, which is too complicated to explain in a comment
    if isPrime(n) or n <= 1:
        # print(n ," is prime")
        factors.append(n)
    else:
        a,b = getFirstFactors(n)
        primeFactorize(a, factors)
        primeFactorize(b, factors)

def getFirstFactors(n): # returns the first factor and the number divided by that factor
    for i in range(2,n):
        if n % i == 0:
            # print("returning",n,"/",i)
            return (i,n//i)

#find GCF and LCM of two positive integers less than 100, and tell if the numbers are relativly prime
