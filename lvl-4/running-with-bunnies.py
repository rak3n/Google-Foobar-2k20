from itertools import permutations, combinations, chain
INF=10000

def bellman_ford(arr, start):
    global INF
    visited=[]
    for i in range(len(arr)):
        visited.append(INF)

    visited[start]=0

    for i in range(len(arr)-1):
        for k in range(len(arr)):
            for j in range(len(arr)):
                if arr[k][j] + visited[k] < visited[j]:
                    visited[j]=arr[k][j]+visited[k]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if visited[i]+arr[i][j] < visited[j]:
                return -1

    return visited

def ford_warshall(arr):
    distance=[]
    for i in arr:
        distance.append(i)

    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

def rescue_bunnies(path,time):
    n=len(path)-2
    rabbits=range(n)
    result=[]
    """Generating Powerset of rabbits"""
    powerset=list(chain.from_iterable(combinations(rabbits,i) for i in range(n+1)))

    for sub in powerset:
        for perm in permutations(sub):
            total_time=0
            prev,nxt=0,0
            for bunny in perm:
                nxt=bunny+1
                total_time+=path[prev][nxt]
                prev=nxt
            total_time+=path[prev][n+1]
            if total_time <= time and len(sub) > len(result):
                result=list(sub)
                if len(result)==n:
                    break
            else:
                continue
    return result

def solution(times, times_limit):
    if len(times)<3:
        return []

    distance_matrix=[]
    for i in range(len(times)):
        distance=bellman_ford(times,i)
        if type(distance)!=list:
            return range(0,len(times)-2)
        distance_matrix.append(distance)

    short_path=ford_warshall(times)
    #print(short_path)
    return rescue_bunnies(short_path, times_limit)

#case=[[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
#case=[[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
"""case=[
        [0,1,-1],
        [1,0,-1],
        [1,1,0],
        ]"""
"""case=[
        [0,10,10,10, 1],
        [0,0 ,10,10,10],
        [0,10,0 ,10,10],
        [0,10,10,0 ,10],
        [1,1 ,1 ,1 , 0]
        ]"""

"""case=[
        [0,10,10,1,10],
        [10,0,10,10,1],
        [10,1,0,10,10],
        [10,10,1,0,10],
        [1,10,10,10,0],
        ]"""

"""case=[
        [0,1],
        [1,0],
        ]"""

"""case=[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        ]"""
case=[
        [0,5,11,11,1],
        [10,0,1,5,1],
        [10,1,0,4,0],
        [10,-11,5,0,1],
        [10,10,10,10,0]
        ]
print(solution(case,1))
