def solution(pegs):
    m=pegs[1]-pegs[0]-1
    for x in xrange(1,m):
        size=[x]
        for peg in range(1,len(pegs)):
            size.append(pegs[peg] - (pegs[peg-1] + size[-1]))
        if any(d<=0 for d in size):
            continue
        if x==2*size[-1]:
            return  [x,1]
        if x+1==2*size[-1]:
            return [(x*3)+1,3]
        if x+2==2*size[-1]:
            return [(x*3)+2,3]
    return [-1,-1]
print(solution([1, 5, 20]))
