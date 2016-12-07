def isPrime():
    n = int(input("N: "))
    for i in range(1,n): # go thru all numbers 1 to just under the number
        if n % i == 0: # if that number is a factor of the number we are getting from the user
            return False # break out of the function because that number is not a prime
    return True # if we go thru all the numbers up to the imput number and there is not a factor, than this line of code says that that number is prime
