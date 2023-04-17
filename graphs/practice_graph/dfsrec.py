def dfs(graph,start):
    print(start)
    for i in graph[start]:
        dfs(graph,i)

graph={
        'a':['b','c'],
        'b':['d'],
        'c':['d'],
        'd':[]
        }



dfs(graph,'a')
