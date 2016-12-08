import math

def isPrime(n):
    topLimit = math.ceil(math.sqrt(n))
    for i in range(2,topLimit): # go thru all numbers 1 to just under the number
        if n % i == 0: # if that number is a factor of the number we are getting from the user
            return False # break out of the function because that number is not a prime
    return True # if we go thru all the numbers up to the imput number and there is not a factor, than this line of code says that that number is prime

def v1(): #easy to understand version
    for i in range(3,10001,2): #only check odds, the third number in range is the number you increment by
        # print(i, i+2) #debug code
        if isPrime(i) and isPrime(i+2): #uses function that we defined at top
            print(i,i+2,"are twin primes")


def v2(): #a bit faster, but weird and complicated
    l = [(x,isPrime(x)) for x in range(3,10001,2)]
    for i in range(len(l)-1):
        # print(l[i],l[i+1]) #debug code
        if l[i][1] and l[i+1][1]:
            print(l[i][0],l[i+1][0])
