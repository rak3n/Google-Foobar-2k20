
def solution(l):
    size=len(l)
    result=[]
    """for i in range(size-1):
        for j in range(i+1,size-1):
            if l[i]<=l[j] and (l[j]%l[i])==0:
                for k in range(j+1,size):
                    if l[j]<=l[k] and (l[k]%l[j])==0:
                        if [l[i],l[j],l[k]] not in result:
                            result.append([l[i],l[j],l[k]])
    """
    m=max(l)
    for i in l[:len(l)-2]:
        for j in range(i,m+1,i):
            if j in l[l.index(i)+1:]:
                for k in range(j,m+1,j):
                    if k in l[l.index(j)+1:]:
                        result.append([i,j,k])
    
    """
    count=[]
    for i in range(size-1,0,-1):
        cnt=0
        for j in range(i-1,-1,-1):
            if l[i]%l[j]==0:
                cnt+=1
        #print(cnt)
        count.append(cnt)
    
    for i in count:
        if i>0:
            result+=(i-1)
        else:
            result+=i
    """
    #print(result)
    return len(result)

def main():
    l=[]
    for i in range(1,2001):
        l.append(i)
    print(solution(l))


main()

