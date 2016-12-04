a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
def v1(a,b): #a smaller than b
    s = 0
    for i in range(a,b+1):
            s+=i
    print('The sum of the integers between',a,'and',b,'is',s)

def v2(a,b): # a can be larger than b
    s = 0
    if a>b:
        a,b = b,a
    for i in range(a,b+1):
            s+=i
    print('The sum of the integers between',a,'and',b,'is',s)

def v3(a,b): # only even numbers
    s = 0
    if a>b:
        a,b = b,a
    for i in range(a,b+1):
            if i % 2 ==0:
                s+= i
    print('The sum of the EVEN integers between',a,'and',b,'is',s)

def v4(a,b):
    if a>b:
        a,b = b,a
    print(sum((x for x in range(a,b+1) if x % 2 == 0)))



# v1(a, b)
# v2(a, b)
# v3(a, b)
v4(a, b)
