import math

#prime number check function
def check_prime(n):
    if n == 1: 
        return False
     
    for x in range(2, (int)(math.sqrt(n))+1): 
        if n % x == 0: 
            return False 
    return True

#this is the solution
def manipulate_generator(g,n):
      # Enter your code here
    if check_prime(n+1):
        next(g)
        manipulate_generator(g, n+1)
  	pass


# the code below is the default/driver code by hackerrank
def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(raw_input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print n 
    manipulate_generator(g, n)
