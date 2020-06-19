
#It is a Beatty sequence, where precision is the key. Really Beautiful ...
from decimal import *

getcontext().prec=100

sqr=(Decimal(2).sqrt()-1)

def n_dash(n):
    return int(sqr*n)
    
def solve(n):
    #print(n)
    if n==0:
        return 0
    return n*n_dash(n) + n*(n+1)/2 - n_dash(n)*(1+n_dash(n))/2 - solve(n_dash(n)) 

def solution(s):
    ret=solve(long(s))
    #print(ceil(ret))
    return str(int(ret))

print(solution('5'))
print(solution('77'))
print(solution(10**100))

