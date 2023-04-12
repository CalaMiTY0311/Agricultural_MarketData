"""
def dfs(graph, start_node):
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
        
    return visited

print(dfs(graph, 'A'))
"""

"""
def dfs(graph, start_node):
    stack = [start_node]
    visited=[]
    while stack:
        node = stack.pop()
        visited.append(node)
        for check_node in graph[node]:
            if check_node not in visited:
                stack.append(check_node)
    return visited

print(dfs(graph, 1))


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited

print(dfs_stack(graph,1))
"""
"""
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
"""
"""
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

def dfs(graph, start):
     stack, visited = list(), list()
     stack.append(start)
     
     while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

print(dfs(graph,'A'))
"""

"""
백준 4963
import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
if x<0 or x>=h or y<0 or y>=w:
return False

if graph[x][y]==1:
	graph[x][y]=0
	dfs(x-1,y)
	dfs(x+1,y)
	dfs(x,y-1)
	dfs(x,y+1)
	dfs(x-1,y+1)
	dfs(x+1,y-1)
	dfs(x-1,y-1)
	dfs(x+1,y+1)
	return True
return False
while True:
w, h = map(int,input().split())
if h==0 or w==0:
break
graph = []
answer = 0
for i in range(h):
graph.append(list(map(int,input().split())))

for i in range(h):
	for j in range(w):
		if dfs(i,j)==True:
			answer+=1

print(answer)
"""