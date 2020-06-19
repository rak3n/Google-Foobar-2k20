"""
This one is an failed aproach all due to precision problem
but V2 of this works like a charm 
"""
from math import sqrt,hypot,atan2,degrees

def upper(ite,en,y1,y2,x1,x2):
    pos=[i for i in en]
    position=[]
    for i in range(ite):
        if i%2==0:
            pos[1]+=(2*y2)
        else:
            pos[1]+=(2*y1)
    
    position.append(pos)
    lpos,rpos=[i for i in pos],[i for i in pos]
    
    for i in range(ite):
        if i%2==0:
            lpos[0]-=(2*x1)
            rpos[0]+=(2*x2)
        else:
            lpos[0]-=(2*x2)
            rpos[0]+=(2*x1)
    
        position.append([j for j in lpos])
        position.append([j for j in rpos])
    
    return position

def lower(ite,en,y1,y2,x1,x2):
    pos=[i for i in en]
    position=[]
    for i in range(ite):
        if i%2==0:
            pos[1]-=(2*y1)
        else:
            pos[1]-=(2*y2)
    
    position.append(pos)
    lpos,rpos=[i for i in pos],[i for i in pos]
    
    for i in range(ite):
        if i%2==0:
            lpos[0]-=(2*x1)
            rpos[0]+=(2*x2)
        else:
            lpos[0]-=(2*x2)
            rpos[0]+=(2*x1)
        position.append([j for j in lpos])
        position.append([j for j in rpos])
    
    return position

def right(ite,en,y1,y2,x1,x2):
    pos=[i for i in en]
    position=[]
    for i in range(ite):
        if i%2==0:
            pos[0]+=2*x2
        else:
            pos[0]+=2*x1
    
    position.append(pos)
    lpos,upos=[i for i in pos],[i for i in pos]
    
    for i in range(ite):
        if i%2==0:
            lpos[1]-=(2*y1)
            upos[1]+=(2*y2)
        else:
            lpos[1]-=(2*y2)
            upos[1]+=(2*y1)
        position.append([j for j in lpos])
        position.append([j for j in upos])
    
    return position

def left(ite,en,y1,y2,x1,x2):
    pos=[i for i in en]
    position=[]
    for i in range(ite):
        if i%2==0:
            pos[0]-=2*x1
        else:
            pos[0]-=2*x2
    
    position.append(pos)
    lpos,upos=[i for i in pos],[i for i in pos]
    
    for i in range(ite):
        if i%2==0:
            lpos[1]-=(2*y1)
            upos[1]+=(2*y2)
        else:
            lpos[1]-=(2*y2)
            upos[1]+=(2*y1)
        position.append([j for j in lpos])
        position.append([j for j in upos])
    
    return position
    

def get_dist(A,B):
    x1,y1=A[0],A[1]
    x2,y2=B[0],B[1]
    d=hypot((x1-x2),(y1-y2))
    return d


def gen_points(length, pos, tpos,mDist):
    hx1=pos[0]
    hx2=length[0]-hx1
    hy1=pos[1]
    hy2=length[1]-hy1
    
    ex1=tpos[0]
    ex2=length[0]-ex1
    ey1=tpos[1]
    ey2=length[1]-ey1
    
    scoreH=[]
    scoreE=[]
    
    q=False
    
    hit = 0
    i=1
    
    while 1:
        
        HeroImage=upper(i,pos,hy1,hy2,hx1,hx2)
        EnemyImage=upper(i,tpos,ey1,ey2,ex1,ex2)
        #print(HeroImage, EnemyImage)
        for hero,target in zip(HeroImage, EnemyImage):
            if get_dist(pos,target) <= mDist and target not in scoreE :
                #print("upper")
                scoreE.append(target)
                scoreH.append(hero)
                hit+=1
            
        
        HeroImage=lower(i,pos,hy1,hy2,hx1,hx2)
        EnemyImage=lower(i,tpos,ey1,ey2,ex1,ex2)
        
        for hero,target in zip(HeroImage, EnemyImage):
            if get_dist(pos,target) <= mDist and target not in scoreE:
                #print("lower")
                scoreE.append(target)
                scoreH.append(hero)
                hit+=1

        HeroImage=left(i,pos,hy1,hy2,hx1,hx2)
        EnemyImage=left(i,tpos,ey1,ey2,ex1,ex2)
        #print(HeroImage, EnemyImage)
        for hero,target in zip(HeroImage, EnemyImage):
            if get_dist(pos,target) <= mDist and target not in scoreE:
                #print("left")
                scoreE.append(target)
                scoreH.append(hero)
                hit+=1

        HeroImage=right(i,pos,hy1,hy2,hx1,hx2)
        EnemyImage=right(i,tpos,ey1,ey2,ex1,ex2)
        #print(HeroImage, EnemyImage)
        for hero,target in zip(HeroImage, EnemyImage):
            if get_dist(pos,target) <= mDist and target not in scoreE:
                #print("right")
                scoreE.append(target)
                scoreH.append(hero)
                hit+=1
        
        if hit==0:
            return scoreH,scoreE
        else:
            hit=0
        i+=1


def get_angle(A,B):
    x,y=(B[0]-A[0]),(B[1]-A[1])
    return degrees(atan2(y,x))

def filter_angle(length,hero, enemy, pointsH,pointsE):
    angle=[]
    ex_angle=get_angle(hero,enemy)
    angle.append(ex_angle)
    if ex_angle<=0:
        angle.append(ex_angle+180)
    else:
        angle.append(ex_angle-180)
    
    corner=[[0,0],[0,length[1]],length,[length[0],0]]
    for i in corner:
        angle.append(get_angle(hero, i))
     
    result=set()
    for i,j  in zip(pointsH,pointsE):
        tem=get_angle(hero,i)
        if tem not in angle:
            angle.append(tem)
        tem=get_angle(hero,j)
        if tem not in angle:
            angle.append(tem)
            result.add(tem)
            
    #print(result)
    return result

def solution(dimensions, your_position, guard_position, distance):
    
   
    pH,pE=gen_points(dimensions,your_position, guard_position,distance)
    #points=gen_pointsV2(dimensions,your_position, guard_position,distance)
    #print(points)
    
    hits=filter_angle(dimensions,your_position,guard_position,pH,pE)
    if get_dist(your_position,guard_position)<=distance:
        #print(len(hits)+1)
        return len(hits)+1
    else:
        #print(len(hits))
        return len(hits)
       
print solution([3,2], [1,1], [2,1], 4)
print solution([300,275], [150,150], [185,100], 500)
print solution([2,5], [1,2], [1,4], 11)#-->27  
print solution([3,2], [1,1], [2,1], 1)#-->1
#solution([3,2], [1,1], [2,1], 1) #-->1
#solution([4,3], [1,1], [3,2], 3)#-->1 
print solution([42,59],[34,44],[6,34],1000)
#solution([2,5],[1,2],[1,4],5000)
