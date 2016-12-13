from IsPrime import isPrime

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
