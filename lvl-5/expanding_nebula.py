import copy
o={0:(1,0),1:(0)}

x={0:(0,1),1:(1,0)}


"""
o={1:0,0:1,2:0} #Gass cell
x={0:(0,3),1:(1,2,3),2:(1,2,3),3:(0,1,2,3)} #no gas cell
def row_generate(g):
    n=len(g[0])+1
    
    prd=[]
    first=True
    
    for i in g:
        prd=[]
        first=True
        for item in i:
            sr=[]
            if item:
                if first:
                    prd=[[0,1],[0,2],[1,0],[2,0]]
                else:
                    new_prd=[]
                    size=len(prd)
                    for index in range(size):
                        if prd[index][-1]!=3:
                            prd[index].append(o[prd[index][-1]])
                            if prd[index][-1]==0:
                                prd[index].append(2)
                            new_prd.append(prd[index])
                            
                    prd=copy.deepcopy(new_prd)
            else:
                if first:
                    prd=[[0,0],[0,3],[1,2],[1,3],[1,1],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
                else:
                    size=len(prd)
                    new_prd=[]
                    for index in range(size):
                        tmp=copy.deepcopy(prd[index])
                        for code in x[tmp[-1]]:
                            tmp.extend([code])
                            new_prd.append(copy.deepcopy(tmp))
                            tmp.pop()
                    prd=copy.deepcopy(new_prd)
            first=False
        print('row:{0}'.format(prd))
"""

def row_generate(g):
    
    #result=[]
    Ml=[]
    for i in g:
        upper=[]
        lower=[]
        first=True
        for item in i:
            if item:
                if first:
                    upper=['00','10','01','00']
                    lower=['01','00','00','10']
                else:
                    new_U,new_L=[],[]
                    size=len(upper)
                    space=[]
                    for index in range(size):
                        if upper[index][-1]=='0' and lower[index][-1]=='0':
                            space=['10','01']
                        if (upper[index][-1]=='1' and lower[index][-1]=='0') or (upper[index][-1]=='0' and lower[index][-1]=='1'):
                            space=['00']
                        
                        if not (upper[index][-1]=='1' and lower[index][-1]=='1'):
                            tmpU=copy.deepcopy(upper[index])
                            tmpL=copy.deepcopy(lower[index])
                            for code in space:
                                new_U.append(tmpU+code[0])
                                new_L.append(tmpL+code[1])
                            
                    upper=copy.deepcopy(new_U)
                    lower=copy.deepcopy(new_L)
            else:
                if first:
                    upper=['00','00','10','10','10','01','01','01','11','11','11','11']
                    lower=['00','11','10','01','11','10','01','11','00','01','10','11']
                else:
                    new_U,new_L=[],[]
                    size=len(upper)
                    space=[]
                    for index in range(size):
                        if (upper[index][-1]=='1' and lower[index][-1]=='0') or (upper[index][-1]=='0' and lower[index][-1]=='1'):
                            space=['10','01','11']
                        if upper[index][-1]=='0' and lower[index][-1]=='0':
                            space=['11']
                        if upper[index][-1]=='1' and lower[index][-1]=='1':
                            space=['00','10','11','01']
                            
                        tmpU=copy.deepcopy(upper[index])
                        tmpL=copy.deepcopy(lower[index])
                        for code in space:
                            new_U.append(tmpU+code[0])
                            new_L.append(tmpL+code[1])
                            
                    upper=copy.deepcopy(new_U)
                    lower=copy.deepcopy(new_L)
            first=False
            print(upper)
            print(lower)
        return
        #Ml=[int(val,2) for val in lower] 
        #print([int(val,2) for val in upper])
        #print([int(val,2) for val in lower])
        Ml.append(len(upper))
    
    print(Ml)
                        
        
def solution(g):
     row_generate(g)
     
#solution([[True, False, True], [False, True, False], [True, False, True]])
#solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
