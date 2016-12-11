import unittest #to run tests to make sure that our function is working as we intended it to

def isPrime(n):
    if n <= 1: # if the number is negative, zero, or one, it is, by definition not prime
        return False

    for i in range(2,n): # go thru all numbers 2 to just under the number
        if n % i == 0: # if that number is a factor of the number we are getting from the user
            return False # break out of the function because that number is not a prime

    return True # if we go thru all the numbers up to the imput number and there is not a factor, than this line of code says that that number is prime

class TestIsPrime(unittest.TestCase): #set up a test suite

    def testZero(self): #make sure that zero returns false
        self.assertFalse(isPrime(0))

    def testOne(self): #make sure that one returns false
        self.assertFalse(isPrime(1))

    def testPositiveIntegers(self): #check numbers two thru 7 inclusive
        self.assertEqual(
            [isPrime(x) for x in range(2,8)],
            [True,True,False,True,False,True]
        ) #make sure that these two lists line up

    def testNegativeIntegers(self): #make sure that negative numbers return false
        self.assertFalse(isPrime(-1))
        self.assertFalse(isPrime(-2))

if __name__ == "__main__": # if we are running this file on its own, or in other words, as "main", then run our test suite. this will not be called if we import this file to be used in another program, but only if we run this file itself. 
    unittest.main()
