count=0
def solution(n):
    global count
    n=int(n)
    while n>1:
        if n%2==0:
            n=n//2
        else:
            a=n+1
            b=n-1
            ac=bc=0
            while a%2==0:
                a=a//2
                ac+=1
            while b%2==0:
                b=b//2
                bc+=1

            if ac>bc and n!=3:
                n+=1
            else:
                n-=1

        count+=1

    return count

print(solution('768'))
