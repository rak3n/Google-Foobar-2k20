def to_base_n(num,base):
    result=''
    while num>0:
        result+=str(num%base)
        num=int(num / base)

    return result[::-1]

def to_base_10(num,base):
    power=1
    result=0
    for i in range(len(num)-1,-1,-1):
        result+=int(num[i])*power
        power*=base

    return result 

def solution(n, b):
    stack=[]
    z=n
    while 1:
        x=''.join(sorted(list(z)))
        y=''.join(sorted(list(z),reverse=1))
        x=to_base_10(x,b)
        y=to_base_10(y,b)
        z=y-x
        z=to_base_n(z,b)
        if z==0:
            return 1
        if z in stack:
            return len(stack)-stack.index(z)
        else:
            stack.append(z)

print(solution('1211',10))
