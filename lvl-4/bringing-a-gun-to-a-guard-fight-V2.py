"""
The most easiest difficult problem
its all about thinking in right reflection :}
Took the most of my time but what a great ray tracing problem
Absolutely love it....
"""
from math import sqrt,atan2

def gen_reflection(mdist,en,y1,y2):
    pos=en
    position=[]
    i=0
    position.append(pos)
    while pos<=mdist:
        if i%2==0:
            pos+=(2*y2)
        else:
            pos+=(2*y1)
        i+=1
        position.append(pos)
    l=len(position)
    for i in range(l):
        position.append(-1*position[i])    
    return position

def gen_points(length, pos, tpos,mDist):
    hx1=pos[0]
    hx2=length[0]-hx1
    hy1=pos[1]
    hy2=length[1]-hy1
    
    ex1=tpos[0]
    ex2=length[0]-ex1
    ey1=tpos[1]
    ey2=length[1]-ey1
    
    Ex=gen_reflection(mDist, tpos[0], ex1,ex2)
    Ey=gen_reflection(mDist, tpos[1], ey1,ey2)
    
    Hx=gen_reflection(mDist, pos[0], hx1,hx2)
    Hy=gen_reflection(mDist, pos[1], hy1,hy2)
    
    #print([Ex,Ey])
    #print([Hx,Hy])
    
    mirrored=[[Hx,Hy],[Ex,Ey]]
    res = set()
    angles_dist = {}

    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = atan2((pos[1]-k), (pos[0]-j))
                l = sqrt((pos[0]-j)**2 + (pos[1]-k)**2)
                if [j, k] != pos and mDist >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            res.add(beam)
                            #print([j,k])
    return len(res)
    


def solution(dimensions, your_position, guard_position, distance):
    hits=gen_points(dimensions,your_position, guard_position,distance)
    return hits
    
    
#print solution([2,5],[1,2],[1,4],50)#->503
#print solution([3,2], [1,1], [2,1], 4)#->7
#print solution([300,275], [150,150], [185,100], 500)#->9
#print solution([2,5], [1,2], [1,4], 11)#->27
#print solution([42,59],[34,44],[6,34],5000)#->30904
print solution([2,5],[1,2],[1,4],1000)#->198985
