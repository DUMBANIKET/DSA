def dfs(graph,start):
    stack=[start]
    while len(stack)>0:
        cur=stack.pop()
        print(cur)
        for neigh in graph[cur]:
            stack.append(neigh)
            #print(neigh)


graph={
        
        'a':['b','c'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':[],
        'f':[]
        
        }

dfs(graph,'a')
